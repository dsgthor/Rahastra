#!/usr/bin/env python3
"""
DropVault Backend - Zero-Knowledge File Sharing Server
Flask backend for handling encrypted file storage and retrieval
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import json
import time
import uuid
import threading
from datetime import datetime
import tempfile
import shutil
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
STORAGE_DIR = os.path.join(tempfile.gettempdir(), 'dropvault_storage')
CLEANUP_INTERVAL = 300  # 5 minutes
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
MAX_STORAGE_SIZE = 1 * 1024 * 1024 * 1024  # 1GB total

# Ensure storage directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)

class FileManager:
    """Manages file storage, retrieval, and cleanup operations"""
    
    def __init__(self):
        self.files = {}  # In-memory index for faster access
        self.load_existing_files()
        self.start_cleanup_thread()
    
    def load_existing_files(self):
        """Load existing files from storage directory on startup"""
        try:
            for item in os.listdir(STORAGE_DIR):
                item_path = os.path.join(STORAGE_DIR, item)
                if os.path.isdir(item_path):
                    metadata_file = os.path.join(item_path, 'metadata.json')
                    if os.path.exists(metadata_file):
                        with open(metadata_file, 'r') as f:
                            metadata = json.load(f)
                            self.files[item] = {
                                'metadata': metadata,
                                'path': item_path,
                                'created': os.path.getctime(item_path)
                            }
        except Exception as e:
            print(f"Error loading existing files: {e}")
    
    def store_file(self, file_data, metadata, note_data=None):
        """Store encrypted file with metadata"""
        file_id = str(uuid.uuid4())
        file_dir = os.path.join(STORAGE_DIR, file_id)
        
        try:
            # Create directory for this file
            os.makedirs(file_dir, exist_ok=True)
            
            # Save encrypted file data
            data_path = os.path.join(file_dir, 'data.enc')
            with open(data_path, 'wb') as f:
                f.write(file_data)
            
            # Save metadata
            metadata_path = os.path.join(file_dir, 'metadata.json')
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f)
            
            # Save encrypted note if provided
            if note_data:
                note_path = os.path.join(file_dir, 'note.enc')
                with open(note_path, 'wb') as f:
                    f.write(note_data)
            
            # Update in-memory index
            self.files[file_id] = {
                'metadata': metadata,
                'path': file_dir,
                'created': time.time()
            }
            
            print(f"File stored: {file_id} ({metadata.get('filename', 'unknown')})")
            return file_id
            
        except Exception as e:
            print(f"Error storing file: {e}")
            # Clean up on error
            if os.path.exists(file_dir):
                shutil.rmtree(file_dir, ignore_errors=True)
            raise
    
    def get_file_info(self, file_id):
        """Get file metadata and check if file exists"""
        if file_id not in self.files:
            return None
        
        file_info = self.files[file_id]
        metadata = file_info['metadata']
        
        # Check if file has expired
        if metadata.get('expiry') and time.time() * 1000 > metadata['expiry']:
            self.delete_file(file_id)
            return None
        
        return file_info
    
    def get_file_data(self, file_id):
        """Get encrypted file data"""
        file_info = self.get_file_info(file_id)
        if not file_info:
            return None
        
        data_path = os.path.join(file_info['path'], 'data.enc')
        if not os.path.exists(data_path):
            return None
        
        try:
            with open(data_path, 'rb') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file data: {e}")
            return None
    
    def get_file_note(self, file_id):
        """Get encrypted note data if it exists"""
        file_info = self.get_file_info(file_id)
        if not file_info:
            return None
        
        note_path = os.path.join(file_info['path'], 'note.enc')
        if not os.path.exists(note_path):
            return None
        
        try:
            with open(note_path, 'rb') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading note data: {e}")
            return None
    
    def delete_file(self, file_id):
        """Delete a file and its metadata"""
        if file_id in self.files:
            file_path = self.files[file_id]['path']
            try:
                if os.path.exists(file_path):
                    shutil.rmtree(file_path)
                del self.files[file_id]
                print(f"File deleted: {file_id}")
                return True
            except Exception as e:
                print(f"Error deleting file {file_id}: {e}")
                return False
        return False
    
    def cleanup_expired_files(self):
        """Remove expired files and enforce storage limits"""
        current_time = time.time() * 1000
        expired_files = []
        
        # Find expired files
        for file_id, file_info in self.files.items():
            metadata = file_info['metadata']
            if metadata.get('expiry') and current_time > metadata['expiry']:
                expired_files.append(file_id)
        
        # Delete expired files
        for file_id in expired_files:
            self.delete_file(file_id)
        
        # Check storage size and remove oldest files if needed
        self.enforce_storage_limits()
        
        if expired_files:
            print(f"Cleaned up {len(expired_files)} expired files")
    
    def enforce_storage_limits(self):
        """Enforce maximum storage size by removing oldest files"""
        try:
            total_size = 0
            file_sizes = []
            
            for file_id, file_info in self.files.items():
                file_path = file_info['path']
                size = self.get_directory_size(file_path)
                total_size += size
                file_sizes.append((file_id, size, file_info['created']))
            
            if total_size > MAX_STORAGE_SIZE:
                # Sort by creation time (oldest first)
                file_sizes.sort(key=lambda x: x[2])
                
                # Remove oldest files until under limit
                for file_id, size, created in file_sizes:
                    if total_size <= MAX_STORAGE_SIZE:
                        break
                    self.delete_file(file_id)
                    total_size -= size
                    print(f"Removed old file {file_id} to free space")
        
        except Exception as e:
            print(f"Error enforcing storage limits: {e}")
    
    def get_directory_size(self, directory):
        """Calculate total size of directory"""
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(directory):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if os.path.exists(filepath):
                        total_size += os.path.getsize(filepath)
        except Exception:
            pass
        return total_size
    
    def start_cleanup_thread(self):
        """Start background thread for periodic cleanup"""
        def cleanup_worker():
            while True:
                try:
                    time.sleep(CLEANUP_INTERVAL)
                    self.cleanup_expired_files()
                except Exception as e:
                    print(f"Cleanup thread error: {e}")
        
        thread = threading.Thread(target=cleanup_worker, daemon=True)
        thread.start()
        print("Cleanup thread started")
    
    def get_stats(self):
        """Get storage statistics"""
        total_files = len(self.files)
        total_size = sum(self.get_directory_size(info['path']) for info in self.files.values())
        
        return {
            'total_files': total_files,
            'total_size': total_size,
            'max_size': MAX_STORAGE_SIZE,
            'storage_usage_percent': (total_size / MAX_STORAGE_SIZE) * 100
        }

# Initialize file manager
file_manager = FileManager()

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file upload with encryption metadata"""
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if not file or not file.filename:
            return jsonify({'error': 'Invalid file'}), 400
        
        # Check file size
        file_data = file.read()
        if len(file_data) > MAX_FILE_SIZE:
            return jsonify({'error': f'File too large. Maximum size: {MAX_FILE_SIZE // (1024*1024)}MB'}), 413
        
        # Get metadata
        metadata_str = request.form.get('metadata')
        if not metadata_str:
            return jsonify({'error': 'No metadata provided'}), 400
        
        try:
            metadata = json.loads(metadata_str)
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid metadata format'}), 400
        
        # Validate required metadata fields
        required_fields = ['filename', 'filetype', 'size', 'uploadTime', 'expiry', 'oneTime', 'hasPassword', 'iv']
        for field in required_fields:
            if field not in metadata:
                return jsonify({'error': f'Missing required metadata field: {field}'}), 400
        
        # Get optional encrypted note
        note_data = None
        if 'note' in request.files:
            note_file = request.files['note']
            note_data = note_file.read()
        
        # Store the file
        file_id = file_manager.store_file(file_data, metadata, note_data)
        
        return jsonify({
            'success': True,
            'id': file_id,
            'message': 'File uploaded successfully'
        })
    
    except Exception as e:
        print(f"Upload error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/file/<file_id>', methods=['GET'])
def get_file_info(file_id):
    """Get file metadata and check if file exists"""
    try:
        file_info = file_manager.get_file_info(file_id)
        if not file_info:
            return jsonify({'error': 'File not found or expired'}), 404
        
        metadata = file_info['metadata']
        
        # Don't return sensitive data in metadata
        safe_metadata = metadata.copy()
        
        return jsonify({
            'success': True,
            'metadata': safe_metadata,
            'exists': True
        })
    
    except Exception as e:
        print(f"Get file info error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/file/<file_id>/data', methods=['GET'])
def get_file_data(file_id):
    """Get encrypted file data"""
    try:
        file_data = file_manager.get_file_data(file_id)
        if file_data is None:
            return jsonify({'error': 'File not found or expired'}), 404
        
        # Create a temporary file to serve the data
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(file_data)
        temp_file.close()
        
        # Clean up temp file after sending
        def cleanup_temp():
            try:
                os.unlink(temp_file.name)
            except:
                pass
        
        # Schedule cleanup
        threading.Timer(60, cleanup_temp).start()
        
        return send_file(
            temp_file.name,
            as_attachment=True,
            download_name='encrypted_data',
            mimetype='application/octet-stream'
        )
    
    except Exception as e:
        print(f"Get file data error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/file/<file_id>/note', methods=['GET'])
def get_file_note(file_id):
    """Get encrypted note data"""
    try:
        note_data = file_manager.get_file_note(file_id)
        if note_data is None:
            return jsonify({'error': 'Note not found'}), 404
        
        # Create a temporary file to serve the note data
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(note_data)
        temp_file.close()
        
        # Clean up temp file after sending
        def cleanup_temp():
            try:
                os.unlink(temp_file.name)
            except:
                pass
        
        threading.Timer(60, cleanup_temp).start()
        
        return send_file(
            temp_file.name,
            as_attachment=True,
            download_name='encrypted_note',
            mimetype='application/octet-stream'
        )
    
    except Exception as e:
        print(f"Get file note error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/file/<file_id>', methods=['DELETE'])
def delete_file(file_id):
    """Delete a file (used for one-time downloads)"""
    try:
        success = file_manager.delete_file(file_id)
        if success:
            return jsonify({'success': True, 'message': 'File deleted'})
        else:
            return jsonify({'error': 'File not found'}), 404
    
    except Exception as e:
        print(f"Delete file error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get server statistics"""
    try:
        stats = file_manager.get_stats()
        return jsonify({
            'success': True,
            'stats': stats
        })
    except Exception as e:
        print(f"Get stats error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'File too large'}), 413

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# Add security headers
@app.after_request
def after_request(response):
    # CORS headers are handled by flask-cors
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == '__main__':
    print("=" * 60)
    print("🔐 DropVault Backend Server Starting...")
    print("=" * 60)
    print(f"📁 Storage Directory: {STORAGE_DIR}")
    print(f"📊 Max File Size: {MAX_FILE_SIZE // (1024*1024)}MB")
    print(f"💾 Max Storage Size: {MAX_STORAGE_SIZE // (1024*1024*1024)}GB")
    print(f"🧹 Cleanup Interval: {CLEANUP_INTERVAL}s")
    print("=" * 60)
    
    # Start the Flask development server
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )