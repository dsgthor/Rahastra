#!/usr/bin/env python3
"""
DirectDrop Lite - Secure P2P File Transfer
A complete single-file application with HTTPS support
"""

import asyncio
import json
import ssl
import uuid
import logging
from pathlib import Path
from typing import Dict, Optional
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global connection manager
class ConnectionManager:
    def __init__(self):
        self.rooms: Dict[str, Dict[str, WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, room_id: str, role: str):
        await websocket.accept()
        if room_id not in self.rooms:
            self.rooms[room_id] = {}
        self.rooms[room_id][role] = websocket
        logger.info(f"Connected {role} to room {room_id}")
        
        # Notify if both peers are connected
        if len(self.rooms[room_id]) == 2:
            await self.broadcast_to_room(room_id, {"type": "peers_connected"})
    
    def disconnect(self, room_id: str, role: str):
        if room_id in self.rooms and role in self.rooms[room_id]:
            del self.rooms[room_id][role]
            if not self.rooms[room_id]:
                del self.rooms[room_id]
        logger.info(f"Disconnected {role} from room {room_id}")
    
    async def send_to_peer(self, room_id: str, sender_role: str, message: dict):
        if room_id not in self.rooms:
            return
        
        target_role = "receiver" if sender_role == "sender" else "sender"
        if target_role in self.rooms[room_id]:
            await self.rooms[room_id][target_role].send_text(json.dumps(message))
    
    async def broadcast_to_room(self, room_id: str, message: dict):
        if room_id not in self.rooms:
            return
        
        for websocket in self.rooms[room_id].values():
            try:
                await websocket.send_text(json.dumps(message))
            except:
                pass

manager = ConnectionManager()
app = FastAPI(title="DirectDrop Lite")

# HTML Template with embedded frontend
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DirectDrop Lite - Secure P2P File Transfer</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e1e2e 0%, #2d2d3d 100%);
            color: #e0e0e0; min-height: 100vh; display: flex; flex-direction: column;
        }
        .container { max-width: 800px; margin: 0 auto; padding: 20px; flex: 1; }
        .header { text-align: center; margin-bottom: 40px; }
        .header h1 { color: #64ffda; font-size: 2.5rem; margin-bottom: 10px; }
        .header p { opacity: 0.8; font-size: 1.1rem; }
        .card {
            background: rgba(255,255,255,0.05); backdrop-filter: blur(10px);
            border-radius: 16px; padding: 30px; margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        .status { padding: 15px; border-radius: 12px; margin-bottom: 20px; text-align: center; font-weight: 600; }
        .status.disconnected { background: rgba(244,67,54,0.2); border: 1px solid #f44336; color: #ff6b6b; }
        .status.connecting { background: rgba(255,193,7,0.2); border: 1px solid #ffc107; color: #ffd54f; }
        .status.connected { background: rgba(76,175,80,0.2); border: 1px solid #4caf50; color: #81c784; }
        .btn {
            background: linear-gradient(45deg, #64ffda, #00bcd4); color: #000; border: none;
            padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: 600;
            transition: all 0.3s ease; display: inline-block; text-decoration: none;
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(100,255,218,0.3); }
        .btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
        .btn.danger { background: linear-gradient(45deg, #f44336, #e91e63); color: white; }
        .input-group { margin-bottom: 20px; }
        .input-group label { display: block; margin-bottom: 8px; font-weight: 600; color: #64ffda; }
        .input-group input, .input-group select {
            width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.1); color: #e0e0e0; font-size: 16px;
        }
        .input-group input:focus { outline: none; border-color: #64ffda; box-shadow: 0 0 0 2px rgba(100,255,218,0.2); }
        .qr-container { text-align: center; margin: 20px 0; }
        .qr-code { background: white; padding: 20px; border-radius: 12px; display: inline-block; }
        .share-link { 
            background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; 
            word-break: break-all; font-family: monospace; margin: 10px 0;
        }
        .file-drop {
            border: 2px dashed rgba(100,255,218,0.5); border-radius: 12px; padding: 40px;
            text-align: center; cursor: pointer; transition: all 0.3s ease; margin: 20px 0;
        }
        .file-drop:hover, .file-drop.drag-over { border-color: #64ffda; background: rgba(100,255,218,0.1); }
        .file-info {
            background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;
            margin: 15px 0; display: flex; justify-content: space-between; align-items: center;
        }
        .progress-bar {
            width: 100%; height: 8px; background: rgba(255,255,255,0.1);
            border-radius: 4px; overflow: hidden; margin: 10px 0;
        }
        .progress-fill {
            height: 100%; background: linear-gradient(45deg, #64ffda, #00bcd4);
            transition: width 0.3s ease; width: 0%;
        }
        .hidden { display: none; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        @media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }
        .peer-info { 
            background: rgba(100,255,218,0.1); padding: 10px; border-radius: 6px; 
            margin: 10px 0; font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 DirectDrop Lite</h1>
            <p>Secure peer-to-peer file transfer with end-to-end encryption</p>
        </div>

        <div class="card">
            <div id="status" class="status disconnected">⚡ Ready to Connect</div>
            
            <div id="role-selection">
                <div class="input-group">
                    <label>Choose your role:</label>
                    <div class="grid">
                        <button class="btn" onclick="initSender()">📤 Send Files</button>
                        <button class="btn" onclick="showReceiver()">📥 Receive Files</button>
                    </div>
                </div>
            </div>

            <div id="receiver-input" class="hidden">
                <div class="input-group">
                    <label>Enter Room Code:</label>
                    <input type="text" id="room-code-input" placeholder="Paste room code here...">
                    <button class="btn" onclick="joinRoom()" style="margin-top: 10px;">Connect</button>
                </div>
            </div>

            <div id="sender-setup" class="hidden">
                <div class="input-group">
                    <label>Optional Password:</label>
                    <input type="password" id="password-input" placeholder="Leave empty for no password">
                </div>
                
                <button class="btn" onclick="createRoom()">Create Room & Wait for Connection</button>
                
                <div id="room-info" class="hidden">
                    <div class="share-link" id="share-link"></div>
                    <div class="qr-container">
                        <div class="qr-code" id="qr-code"></div>
                    </div>
                    <p style="text-align: center; opacity: 0.8; margin-top: 10px;">
                        Share this link or scan the QR code
                    </p>
                </div>
            </div>

            <div id="connection-controls" class="hidden">
                <div class="peer-info" id="peer-info"></div>
                <button class="btn danger" onclick="disconnect()">🔌 Disconnect</button>
            </div>

            <div id="file-transfer" class="hidden">
                <div id="file-drop" class="file-drop">
                    <p>📁 Click here or drag & drop files to send</p>
                    <input type="file" id="file-input" multiple style="display: none;">
                </div>
                
                <div id="file-queue"></div>
            </div>

            <div id="receive-area" class="hidden">
                <h3 style="color: #64ffda; margin-bottom: 15px;">📥 Incoming Files</h3>
                <div id="incoming-files"></div>
            </div>
        </div>
    </div>

    <script>
        let ws = null;
        let pc = null;
        let dataChannel = null;
        let role = null;
        let roomId = null;
        let isConnected = false;
        let fileQueue = [];
        let currentTransfer = null;

        const ICE_SERVERS = [
            { urls: 'stun:stun.l.google.com:19302' },
            { urls: 'stun:stun1.l.google.com:19302' }
        ];

        function updateStatus(message, type = 'disconnected') {
            const status = document.getElementById('status');
            status.textContent = message;
            status.className = `status ${type}`;
        }

        function showElement(id) {
            document.getElementById(id).classList.remove('hidden');
        }

        function hideElement(id) {
            document.getElementById(id).classList.add('hidden');
        }

        function generateRoomId() {
            return 'room-' + Math.random().toString(36).substr(2, 9) + Date.now().toString(36);
        }

        function initSender() {
            role = 'sender';
            hideElement('role-selection');
            showElement('sender-setup');
        }

        function showReceiver() {
            role = 'receiver';
            hideElement('role-selection');
            showElement('receiver-input');
        }

        async function createRoom() {
            roomId = generateRoomId();
            const protocol = location.protocol === 'https:' ? 'wss:' : 'ws:';
            const wsUrl = `${protocol}//${location.host}/ws/${roomId}/sender`;
            
            updateStatus('🔄 Creating room...', 'connecting');
            
            try {
                ws = new WebSocket(wsUrl);
                ws.onopen = () => {
                    updateStatus('⏳ Waiting for receiver...', 'connecting');
                    displayRoomInfo();
                };
                ws.onmessage = handleWebSocketMessage;
                ws.onclose = () => handleDisconnect();
            } catch (error) {
                updateStatus('❌ Failed to create room', 'disconnected');
                console.error('WebSocket error:', error);
            }
        }

        async function joinRoom() {
            const roomCode = document.getElementById('room-code-input').value.trim();
            if (!roomCode) return;

            roomId = roomCode;
            const protocol = location.protocol === 'https:' ? 'wss:' : 'ws:';
            const wsUrl = `${protocol}//${location.host}/ws/${roomId}/receiver`;
            
            updateStatus('🔄 Connecting...', 'connecting');
            
            try {
                ws = new WebSocket(wsUrl);
                ws.onopen = () => updateStatus('⏳ Establishing connection...', 'connecting');
                ws.onmessage = handleWebSocketMessage;
                ws.onclose = () => handleDisconnect();
            } catch (error) {
                updateStatus('❌ Failed to connect', 'disconnected');
                console.error('WebSocket error:', error);
            }
        }

        function displayRoomInfo() {
            const shareLink = `${location.origin}/?room=${roomId}`;
            document.getElementById('share-link').textContent = shareLink;
            
            // Generate QR Code
            const qr = qrcode(0, 'M');
            qr.addData(shareLink);
            qr.make();
            document.getElementById('qr-code').innerHTML = qr.createImgTag(4);
            
            showElement('room-info');
        }

        async function handleWebSocketMessage(event) {
            const message = JSON.parse(event.data);
            
            switch (message.type) {
                case 'peers_connected':
                    await initWebRTC();
                    break;
                case 'offer':
                case 'answer':
                    await pc.setRemoteDescription(new RTCSessionDescription(message));
                    if (message.type === 'offer') {
                        const answer = await pc.createAnswer();
                        await pc.setLocalDescription(answer);
                        ws.send(JSON.stringify(answer));
                    }
                    break;
                case 'ice-candidate':
                    await pc.addIceCandidate(new RTCIceCandidate(message.candidate));
                    break;
                case 'disconnect':
                    handleDisconnect();
                    break;
            }
        }

        async function initWebRTC() {
            pc = new RTCPeerConnection({ iceServers: ICE_SERVERS });
            
            pc.onicecandidate = (event) => {
                if (event.candidate) {
                    ws.send(JSON.stringify({
                        type: 'ice-candidate',
                        candidate: event.candidate
                    }));
                }
            };

            if (role === 'sender') {
                dataChannel = pc.createDataChannel('files', { ordered: true });
                setupDataChannel(dataChannel);
                
                const offer = await pc.createOffer();
                await pc.setLocalDescription(offer);
                ws.send(JSON.stringify(offer));
            } else {
                pc.ondatachannel = (event) => {
                    setupDataChannel(event.channel);
                };
            }
        }

        function setupDataChannel(channel) {
            dataChannel = channel;
            
            dataChannel.onopen = () => {
                isConnected = true;
                updateStatus('✅ Connected - Ready to transfer files!', 'connected');
                hideElement('sender-setup');
                hideElement('receiver-input');
                showElement('connection-controls');
                
                if (role === 'sender') {
                    showElement('file-transfer');
                    setupFileDrop();
                } else {
                    showElement('receive-area');
                }
                
                document.getElementById('peer-info').textContent = 
                    `Connected as ${role} | Room: ${roomId}`;
            };
            
            dataChannel.onmessage = handleFileMessage;
            dataChannel.onclose = () => handleDisconnect();
        }

        function setupFileDrop() {
            const fileDrop = document.getElementById('file-drop');
            const fileInput = document.getElementById('file-input');
            
            fileDrop.onclick = () => fileInput.click();
            fileInput.onchange = (e) => handleFiles(e.target.files);
            
            fileDrop.ondragover = (e) => {
                e.preventDefault();
                fileDrop.classList.add('drag-over');
            };
            
            fileDrop.ondragleave = () => fileDrop.classList.remove('drag-over');
            
            fileDrop.ondrop = (e) => {
                e.preventDefault();
                fileDrop.classList.remove('drag-over');
                handleFiles(e.dataTransfer.files);
            };
        }

        async function handleFiles(files) {
            if (!isConnected) return;
            
            for (let file of files) {
                fileQueue.push(file);
                addFileToQueue(file);
            }
            
            if (!currentTransfer) {
                await processFileQueue();
            }
        }

        function addFileToQueue(file) {
            const fileDiv = document.createElement('div');
            fileDiv.className = 'file-info';
            fileDiv.innerHTML = `
                <span>📄 ${file.name} (${formatFileSize(file.size)})</span>
                <span id="status-${file.name}">⏳ Queued</span>
            `;
            document.getElementById('file-queue').appendChild(fileDiv);
        }

        async function processFileQueue() {
            if (fileQueue.length === 0 || currentTransfer) return;
            
            currentTransfer = fileQueue.shift();
            await sendFile(currentTransfer);
            currentTransfer = null;
            
            setTimeout(() => processFileQueue(), 100);
        }

        async function sendFile(file) {
            const chunkSize = 16384; // 16KB chunks
            const totalChunks = Math.ceil(file.size / chunkSize);
            
            // Send file metadata
            dataChannel.send(JSON.stringify({
                type: 'file-start',
                name: file.name,
                size: file.size,
                totalChunks: totalChunks
            }));
            
            document.getElementById(`status-${file.name}`).textContent = '📤 Sending...';
            
            // Send file chunks
            for (let i = 0; i < totalChunks; i++) {
                const start = i * chunkSize;
                const end = Math.min(start + chunkSize, file.size);
                const chunk = file.slice(start, end);
                const arrayBuffer = await chunk.arrayBuffer();
                
                dataChannel.send(JSON.stringify({
                    type: 'file-chunk',
                    chunkIndex: i,
                    data: Array.from(new Uint8Array(arrayBuffer))
                }));
                
                // Small delay to prevent overwhelming
                if (i % 10 === 0) await new Promise(resolve => setTimeout(resolve, 1));
            }
            
            // Send completion signal
            dataChannel.send(JSON.stringify({
                type: 'file-end',
                name: file.name
            }));
            
            document.getElementById(`status-${file.name}`).textContent = '✅ Sent';
        }

        let incomingFiles = new Map();

        function handleFileMessage(event) {
            const message = JSON.parse(event.data);
            
            switch (message.type) {
                case 'file-start':
                    incomingFiles.set(message.name, {
                        name: message.name,
                        size: message.size,
                        totalChunks: message.totalChunks,
                        receivedChunks: [],
                        progress: 0
                    });
                    addIncomingFile(message.name, message.size);
                    break;
                    
                case 'file-chunk':
                    const fileData = incomingFiles.get(getCurrentFileName());
                    if (fileData) {
                        fileData.receivedChunks[message.chunkIndex] = new Uint8Array(message.data);
                        fileData.progress = (Object.keys(fileData.receivedChunks).length / fileData.totalChunks) * 100;
                        updateFileProgress(fileData.name, fileData.progress);
                    }
                    break;
                    
                case 'file-end':
                    completeFileDownload(message.name);
                    break;
            }
        }

        function getCurrentFileName() {
            // Get the most recent file being transferred
            return Array.from(incomingFiles.keys()).pop();
        }

        function addIncomingFile(name, size) {
            const fileDiv = document.createElement('div');
            fileDiv.className = 'file-info';
            fileDiv.id = `incoming-${name}`;
            fileDiv.innerHTML = `
                <span>📄 ${name} (${formatFileSize(size)})</span>
                <span id="progress-${name}">📥 0%</span>
                <div class="progress-bar">
                    <div class="progress-fill" id="progress-fill-${name}"></div>
                </div>
            `;
            document.getElementById('incoming-files').appendChild(fileDiv);
        }

        function updateFileProgress(name, progress) {
            document.getElementById(`progress-${name}`).textContent = `📥 ${Math.round(progress)}%`;
            document.getElementById(`progress-fill-${name}`).style.width = `${progress}%`;
        }

        function completeFileDownload(name) {
            const fileData = incomingFiles.get(name);
            if (!fileData) return;
            
            // Combine all chunks
            const totalSize = fileData.receivedChunks.reduce((sum, chunk) => sum + chunk.length, 0);
            const completeFile = new Uint8Array(totalSize);
            let offset = 0;
            
            fileData.receivedChunks.forEach(chunk => {
                completeFile.set(chunk, offset);
                offset += chunk.length;
            });
            
            // Create download
            const blob = new Blob([completeFile]);
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = name;
            a.click();
            URL.revokeObjectURL(url);
            
            // Update UI
            document.getElementById(`progress-${name}`).textContent = '✅ Downloaded';
            document.getElementById(`progress-fill-${name}`).style.width = '100%';
            
            incomingFiles.delete(name);
        }

        function formatFileSize(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }

        function disconnect() {
            if (ws) ws.send(JSON.stringify({ type: 'disconnect' }));
            handleDisconnect();
        }

        function handleDisconnect() {
            isConnected = false;
            if (ws) ws.close();
            if (pc) pc.close();
            
            updateStatus('⚡ Disconnected', 'disconnected');
            
            // Reset UI
            hideElement('connection-controls');
            hideElement('file-transfer');
            hideElement('receive-area');
            hideElement('sender-setup');
            hideElement('receiver-input');
            hideElement('room-info');
            showElement('role-selection');
            
            // Clear data
            ws = null;
            pc = null;
            dataChannel = null;
            role = null;
            roomId = null;
            fileQueue = [];
            currentTransfer = null;
            incomingFiles.clear();
            
            document.getElementById('file-queue').innerHTML = '';
            document.getElementById('incoming-files').innerHTML = '';
        }

        // Check for room parameter in URL
        window.onload = () => {
            const urlParams = new URLSearchParams(window.location.search);
            const roomParam = urlParams.get('room');
            if (roomParam) {
                document.getElementById('room-code-input').value = roomParam;
                showReceiver();
            }
        };
    </script>
</body>
</html>'''

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_TEMPLATE

@app.websocket("/ws/{room_id}/{role}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, role: str):
    await manager.connect(websocket, room_id, role)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Handle disconnect message
            if message.get("type") == "disconnect":
                await manager.broadcast_to_room(room_id, {"type": "disconnect"})
                break
            
            # Forward WebRTC signaling messages
            await manager.send_to_peer(room_id, role, message)
            
    except WebSocketDisconnect:
        pass
    finally:
        manager.disconnect(room_id, role)
        # Notify remaining peer of disconnection
        await manager.broadcast_to_room(room_id, {"type": "disconnect"})

def create_ssl_context():
    """Create SSL context for HTTPS"""
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    
    # For development, create self-signed certificate
    cert_file = Path("cert.pem")
    key_file = Path("key.pem")
    
    if not cert_file.exists() or not key_file.exists():
        logger.info("Creating self-signed certificate for HTTPS...")
        import subprocess
        try:
            subprocess.run([
                "openssl", "req", "-x509", "-newkey", "rsa:4096", "-nodes",
                "-out", "cert.pem", "-keyout", "key.pem", "-days", "365",
                "-subj", "/C=US/ST=State/L=City/O=DirectDrop/CN=localhost"
            ], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.warning("OpenSSL not found. HTTPS will not be available.")
            return None
    
    try:
        context.load_cert_chain(cert_file, key_file)
        return context
    except Exception as e:
        logger.warning(f"Failed to load SSL certificate: {e}")
        return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="DirectDrop Lite - Secure P2P File Transfer")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8901, help="Port to bind to")
    parser.add_argument("--https", action="store_true", help="Enable HTTPS")
    parser.add_argument("--cert", help="Path to SSL certificate file")
    parser.add_argument("--key", help="Path to SSL private key file")
    
    args = parser.parse_args()
    
    ssl_context = None
    if args.https:
        if args.cert and args.key:
            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(args.cert, args.key)
        else:
            ssl_context = create_ssl_context()
        
        if ssl_context:
            logger.info(f"Starting DirectDrop Lite with HTTPS on {args.host}:{args.port}")
            logger.info("⚠️  Using self-signed certificate - browsers will show security warning")
        else:
            logger.warning("HTTPS requested but SSL setup failed, falling back to HTTP")
    
    if not ssl_context:
        logger.info(f"Starting DirectDrop Lite on {args.host}:{args.port}")
    
    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        ssl_certfile="cert.pem" if ssl_context and not args.cert else args.cert,
        ssl_keyfile="key.pem" if ssl_context and not args.key else args.key,
        log_level="info"
    )
