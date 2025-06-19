# 🚀 DirectDrop Lite

A secure, peer-to-peer file transfer application that enables direct file sharing between devices without storing files on any server. Built with Python FastAPI and WebRTC for maximum security and performance.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com/)

## ✨ Features

- **🔒 Secure P2P Transfer**: Direct peer-to-peer connection using WebRTC
- **🌐 Web-based Interface**: No desktop app installation required
- **📱 Cross-platform**: Works on any device with a modern web browser
- **🔐 HTTPS Support**: Optional SSL/TLS encryption for web interface
- **📊 Real-time Progress**: Live transfer progress with visual indicators
- **🎯 Simple UI**: Intuitive drag-and-drop interface
- **🔗 Easy Sharing**: QR codes and shareable links for quick connection
- **📁 Multiple Files**: Support for sending multiple files simultaneously
- **🚫 No Server Storage**: Files never touch the server - direct device-to-device transfer
- **⚡ Fast Transfer**: Optimized chunking for efficient large file transfers

## 🛠️ Requirements

- Python 3.8 or higher
- Modern web browser with WebRTC support
- Network connectivity between devices

### Python Dependencies

```bash
fastapi>=0.68.0
uvicorn[standard]>=0.15.0
websockets>=10.0
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/directdrop-lite.git
cd directdrop-lite

# Install dependencies
pip install fastapi uvicorn websockets

# Or install from requirements.txt
pip install -r requirements.txt
```

### 2. Run the Application

```bash
# Basic HTTP server
python directdrop_lite2.py

# With custom host and port
python directdrop_lite2.py --host 0.0.0.0 --port 8080

# Enable HTTPS with self-signed certificate (recommended)
python directdrop_lite2.py --https

# Use custom SSL certificates
python directdrop_lite2.py --https --cert /path/to/cert.pem --key /path/to/key.pem
```

### 3. Access the Application

Open your web browser and navigate to:
- HTTP: `http://localhost:8901`
- HTTPS: `https://localhost:8901` (accept security warning for self-signed cert)

## 📖 Usage Guide

### Sending Files

1. **Choose Role**: Click "📤 Send Files"
2. **Create Room**: Optionally set a password, then click "Create Room & Wait for Connection"
3. **Share Connection**: Share the generated link or QR code with the recipient
4. **Wait for Connection**: The status will update when the receiver connects
5. **Transfer Files**: Drag and drop files or click to select files to send

### Receiving Files

1. **Choose Role**: Click "📥 Receive Files"
2. **Enter Room Code**: Paste the room code shared by the sender
3. **Connect**: Click "Connect" to establish connection
4. **Receive Files**: Files will automatically download when sent

## 🔧 Command Line Options

```bash
usage: directdrop_lite2.py [-h] [--host HOST] [--port PORT] [--https] 
                          [--cert CERT] [--key KEY]

DirectDrop Lite - Secure P2P File Transfer

optional arguments:
  -h, --help     show this help message and exit
  --host HOST    Host to bind to (default: 0.0.0.0)
  --port PORT    Port to bind to (default: 8901)
  --https        Enable HTTPS with self-signed certificate
  --cert CERT    Path to SSL certificate file
  --key KEY      Path to SSL private key file
```

### Examples

```bash
# Run on specific interface and port
python directdrop_lite2.py --host 192.168.1.100 --port 9000

# Enable HTTPS for secure connections
python directdrop_lite2.py --https --port 443

# Use production SSL certificates
python directdrop_lite2.py --https --cert /etc/ssl/certs/mydomain.crt --key /etc/ssl/private/mydomain.key
```

## 🏗️ Architecture

### Components

- **FastAPI Backend**: Handles WebSocket connections and signaling
- **WebRTC Frontend**: Manages peer-to-peer data channels
- **Connection Manager**: Coordinates room-based peer connections
- **File Transfer Protocol**: Custom chunked file transfer over WebRTC

### Data Flow

```
Sender Device ←→ WebSocket Signaling Server ←→ Receiver Device
     ↓                                              ↑
     └─────── Direct WebRTC Data Channel ──────────┘
```

1. **Signaling Phase**: WebSocket server facilitates WebRTC handshake
2. **P2P Connection**: Direct connection established between peers
3. **File Transfer**: Files transferred directly via WebRTC data channels
4. **No Server Storage**: Server only handles connection coordination

## 🔒 Security Features

- **WebRTC Encryption**: All data transfers use DTLS encryption
- **No Server Storage**: Files never stored on the server
- **Room-based Isolation**: Each transfer session is isolated
- **Optional HTTPS**: Secure web interface with SSL/TLS
- **Self-signed Certificates**: Automatic certificate generation for development

## 🌐 Network Configuration

### Firewall Considerations

For optimal connectivity, ensure the following ports are accessible:

- **Application Port**: Default 8901 (configurable)
- **WebRTC Ports**: UDP ports for STUN/TURN (handled automatically)

### STUN Servers

The application uses public STUN servers for NAT traversal:
- `stun:stun.l.google.com:19302`
- `stun:stun1.l.google.com:19302`

For enterprise environments, you may need to configure custom STUN/TURN servers.

## 🔧 Development

### Project Structure

```
directdrop-lite/
├── directdrop_lite2.py    # Main application file
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── cert.pem              # Auto-generated SSL certificate (if using --https)
└── key.pem               # Auto-generated SSL private key (if using --https)
```

### Key Technologies

- **Backend**: FastAPI, Uvicorn, WebSockets
- **Frontend**: Vanilla JavaScript, WebRTC APIs
- **Styling**: Custom CSS with modern design
- **QR Codes**: qrcode-generator library

### Customization

The application is designed as a single-file solution for easy deployment and modification. Key areas for customization:

- **Styling**: Modify the CSS within the `HTML_TEMPLATE`
- **Chunk Size**: Adjust `chunkSize` variable for different transfer speeds
- **STUN Servers**: Modify `ICE_SERVERS` configuration
- **UI Elements**: Customize the HTML template for different branding

## 🚀 Deployment

### Development Deployment

```bash
# Simple local development
python directdrop_lite2.py

# Development with HTTPS
python directdrop_lite2.py --https
```

### Production Deployment

```bash
# Using production certificates
python directdrop_lite2.py --https --cert /path/to/cert.pem --key /path/to/key.pem --host 0.0.0.0 --port 443

# Using reverse proxy (nginx/apache)
python directdrop_lite2.py --host 127.0.0.1 --port 8901
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY directdrop_lite2.py requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8901
CMD ["python", "directdrop_lite2.py", "--host", "0.0.0.0"]
```

```bash
# Build and run
docker build -t directdrop-lite .
docker run -p 8901:8901 directdrop-lite
```

## 🔍 Troubleshooting

### Common Issues

**Connection Failed**
- Ensure both devices are on the same network or have internet connectivity
- Check firewall settings for WebRTC traffic
- Try using HTTPS mode for better compatibility

**Files Not Transferring**
- Verify WebRTC data channel is established (status shows "Connected")
- Check browser console for JavaScript errors
- Ensure sufficient disk space on receiving device

**HTTPS Certificate Warnings**
- Self-signed certificates will trigger browser warnings
- Click "Advanced" → "Proceed to localhost (unsafe)" for development
- Use valid certificates for production deployments

**Large File Transfer Issues**
- Monitor browser memory usage for very large files
- Consider splitting extremely large files (>1GB) into smaller parts
- Ensure stable network connection for duration of transfer

### Browser Compatibility

Tested and supported browsers:
- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

### Network Requirements

- **Bandwidth**: Minimum 1 Mbps for small files, higher for large files
- **Latency**: Lower latency improves transfer initiation
- **NAT Traversal**: Most home/office networks supported via STUN

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test on multiple browsers
- Ensure HTTPS compatibility
- Update documentation for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [WebRTC](https://webrtc.org/) for peer-to-peer communication standards
- [QR Code Generator](https://github.com/davidshimjs/qrcodejs) for QR code functionality

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [GitHub Issues](https://github.com/yourusername/directdrop-lite/issues)
3. Create a new issue with detailed information about your problem

---

**Made with ❤️ for secure file sharing**