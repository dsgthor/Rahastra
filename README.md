# 🔐 Rahastra

**Zero-Knowledge File Sharing with End-to-End Encryption**

Rahastra is a secure, client-side file sharing application that provides end-to-end encryption for your files. All encryption and decryption happens in your browser, ensuring that your data never leaves your device unencrypted.

![Rahastra Interface](https://via.placeholder.com/800x400/000000/e53935?text=Rahastra+Interface)

## ✨ Features

### 🔒 Security Features
- **Zero-Knowledge Architecture**: Files are encrypted client-side before upload
- **AES-256-GCM Encryption**: Military-grade encryption standard
- **Password Protection**: Optional additional password layer with PBKDF2 key derivation
- **Secure Key Generation**: Uses Web Crypto API for cryptographically secure random keys
- **No Server-Side Decryption**: Server never has access to your encryption keys

### 📁 File Management
- **Drag & Drop Interface**: Intuitive file selection
- **Multiple File Upload**: Upload multiple files simultaneously
- **File Preview**: Preview images, PDFs, text files, audio, and video
- **File Type Support**: Supports all file types with appropriate icons
- **Size Validation**: 100MB per file, 500MB total limit

### 🎛️ Advanced Options
- **Auto-Expiry**: Set files to automatically delete after 1 hour to 30 days
- **One-Time Download**: Files automatically delete after first download
- **Private Notes**: Add encrypted notes to your shared files
- **QR Code Generation**: Instant QR codes for easy mobile sharing
- **Real-time Countdown**: Live expiry countdown for time-sensitive files

### 🌐 Sharing & Accessibility
- **Direct Links**: Shareable URLs with embedded encryption keys
- **Web Share API**: Native sharing on supported devices
- **Mobile Responsive**: Works seamlessly on desktop and mobile
- **Offline Preview**: View files without internet connection after download
- **Copy to Clipboard**: One-click link copying

### 🎨 User Experience
- **Dark Theme**: Modern, eye-friendly dark interface
- **Progress Indicators**: Real-time upload progress
- **Toast Notifications**: Clear feedback for all actions
- **Keyboard Shortcuts**: Ctrl+U to upload, Ctrl+Enter to confirm
- **Error Handling**: Graceful error handling with user-friendly messages

## 🚀 Quick Start

### Option 1: Direct Usage
1. Download the `rahastra-app.html` file
2. Open it in any modern web browser
3. Start sharing files securely!

### Option 2: Local Server
```bash
# Clone the repository
git clone https://github.com/yourusername/rahastra.git
cd rahastra

# Serve with Python (or any static file server)
python -m http.server 8000

# Open http://localhost:8000 in your browser
```

### Option 3: GitHub Pages
1. Fork this repository
2. Enable GitHub Pages in repository settings
3. Access your deployment at `https://yourusername.github.io/rahastra`

## 🔧 How It Works

### Encryption Process
1. **File Selection**: User selects files via drag-drop or file picker
2. **Key Generation**: 
   - Without password: AES-256 key generated using Web Crypto API
   - With password: Key derived using PBKDF2 with 100,000 iterations
3. **Encryption**: Files encrypted using AES-GCM with random IV
4. **Storage**: Encrypted data stored (simulated backend in demo)
5. **Link Generation**: Share URL includes file ID and encryption key (in hash fragment)

### Decryption Process
1. **Link Access**: User opens shared link
2. **File Retrieval**: Encrypted file downloaded from storage
3. **Key Extraction**: Encryption key extracted from URL hash or password
4. **Decryption**: File decrypted client-side using Web Crypto API
5. **Preview/Download**: File available for preview or download

### Security Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Device   │    │     Server       │    │  Recipient      │
│                 │    │                  │    │                 │
│ 1. File + Key   │    │ 2. Encrypted     │    │ 4. Encrypted    │
│ 2. Encrypt      │───▶│    File Only     │───▶│    File         │
│ 3. Generate URL │    │ 3. Store Blob    │    │ 5. Decrypt      │
│                 │    │    (No Keys!)    │    │ 6. Access File  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🛠️ Technical Details

### Supported Browsers
- Chrome/Chromium 60+
- Firefox 57+
- Safari 11+
- Edge 79+

*Requires browsers with Web Crypto API support*

### Encryption Specifications
- **Algorithm**: AES-256-GCM
- **Key Derivation**: PBKDF2 with SHA-256 (100,000 iterations)
- **IV Generation**: Cryptographically secure random 12-byte IV per file
- **Salt Generation**: Cryptographically secure random 16-byte salt per password

### File Size Limits
- **Per File**: 100MB maximum
- **Total Upload**: 500MB maximum per session
- **Storage**: Browser memory (no persistent storage)

### Dependencies
- **QR Code Generation**: `qrcode-generator` (1.4.4) from CDNJS
- **Encryption**: Native Web Crypto API
- **No Framework Dependencies**: Pure HTML, CSS, JavaScript

## 📋 Usage Examples

### Basic File Sharing
```javascript
// 1. Select files
// 2. Click "Upload Files"
// 3. Share generated link
// Example link: https://yoursite.com/rahastra?download=file_123#aGVsbG93b3JsZA==
```

### Password Protected Sharing
```javascript
// 1. Select files
// 2. Enter password in "Optional Password Protection"
// 3. Upload files
// 4. Share link (recipient needs password)
// Example link: https://yoursite.com/rahastra?download=file_456
```

### One-Time Sharing
```javascript
// 1. Select files
// 2. Check "One-time download"
// 3. Upload and share
// File automatically deletes after first download
```

## 🔒 Security Considerations

### What's Secure
✅ **Client-side encryption**: Files encrypted before leaving your device  
✅ **Zero-knowledge**: Server never sees your encryption keys  
✅ **Forward secrecy**: Each file has unique encryption key  
✅ **Password protection**: Additional PBKDF2 key derivation  
✅ **Auto-expiry**: Files automatically deleted  
✅ **One-time downloads**: Self-destructing file shares  

### Important Notes
⚠️ **Link Security**: Anyone with the full link can access the file  
⚠️ **Browser Storage**: Files stored in browser memory only  
⚠️ **HTTPS Required**: Always use HTTPS in production  
⚠️ **Key Management**: Keys are in URL hash - share securely  
⚠️ **Demo Limitation**: Current version uses simulated backend  

## 🚧 Development & Deployment

### Local Development
```bash
# No build process required - it's a single HTML file!
# Just open in browser or serve with any static server

# For development with live reload:
npx live-server --port=8080 --host=localhost
```

### Production Deployment

#### Static Hosting (Recommended)
- **Netlify**: Drag and drop deployment
- **Vercel**: Connect GitHub repository
- **GitHub Pages**: Enable in repository settings
- **Firebase Hosting**: `firebase deploy`

#### Server Requirements
- Static file serving capability
- HTTPS support (required for Web Crypto API)
- No server-side processing needed

### Environment Variables
No environment variables required - everything runs client-side!

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Bug Reports
1. Check existing issues first
2. Provide detailed reproduction steps
3. Include browser version and OS
4. Add console error messages if any

### Feature Requests
1. Search existing feature requests
2. Describe the use case clearly
3. Explain why it would be valuable
4. Consider security implications

### Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly in multiple browsers
5. Submit pull request with clear description

### Development Guidelines
- Maintain security-first approach
- Keep single-file architecture
- Ensure mobile responsiveness
- Add appropriate error handling
- Follow existing code style
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 DropVault Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 🆘 Support

### Frequently Asked Questions

**Q: Is my data really secure?**  
A: Yes! All encryption happens in your browser using the Web Crypto API. The server never sees your unencrypted files or encryption keys.

**Q: What happens if I lose the link?**  
A: Unfortunately, there's no way to recover files without the link, as we don't store the encryption keys server-side.

**Q: Can I use this for large files?**  
A: Current limit is 100MB per file. For larger files, consider splitting them or using dedicated large file transfer services.

**Q: Does this work offline?**  
A: File decryption and preview work offline once downloaded, but uploading requires internet connection.

**Q: Is there a mobile app?**  
A: Rahastra is a Progressive Web App (PWA) that works great on mobile browsers. You can "Add to Home Screen" for app-like experience.

### Getting Help
- 📖 Check this README first
- 🐛 [Report bugs](https://github.com/yourusername/rahastra/issues)
- 💡 [Request features](https://github.com/yourusername/rahastra/issues)
- 💬 [Discussions](https://github.com/yourusername/rahastra/discussions)

### Contact
- **Project Maintainer**: [Your Name](mailto:your.email@example.com)
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Website**: https://yourusername.github.io/rahastra

## 🙏 Acknowledgments

- **Web Crypto API**: For making client-side encryption possible
- **QR Code Generator**: For easy mobile sharing
- **Contributors**: Thanks to all who have helped improve Rahastra
- **Security Community**: For feedback on cryptographic implementation
- **Open Source**: Built with and for the open source community

---

**⭐ If you find Rahastra useful, please consider giving it a star on GitHub!**

---

*Made with ❤️ for privacy and security*