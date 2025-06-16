# Contributing to Rahastra

Thank you for your interest in contributing to Rahastra! This document provides guidelines and information for contributors.

## 🤝 Ways to Contribute

### 🐛 Bug Reports
- **Search existing issues** before creating a new one
- **Use the bug report template** when available
- **Provide detailed information** including:
  - Steps to reproduce the issue
  - Expected vs actual behavior
  - Browser version and operating system
  - Console error messages (if any)
  - Screenshots or recordings if applicable

### 💡 Feature Requests
- **Check existing feature requests** to avoid duplicates
- **Describe the problem** your feature would solve
- **Explain the proposed solution** in detail
- **Consider security implications** for new features
- **Provide use cases** and examples

### 📖 Documentation
- **Fix typos** and grammar errors
- **Improve clarity** of existing documentation
- **Add missing documentation** for features
- **Update outdated information**
- **Translate documentation** to other languages

### 💻 Code Contributions
- **Bug fixes** and security improvements
- **New features** that align with project goals
- **Performance optimizations**
- **Accessibility improvements**
- **Browser compatibility fixes**

## 🚀 Getting Started

### Prerequisites
- Modern web browser with Web Crypto API support
- Basic knowledge of HTML, CSS, and JavaScript
- Understanding of cryptographic concepts (for security-related contributions)

### Development Setup
1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/rahastra.git
   cd rahastra
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Set up development environment**:
   ```bash
   # Option 1: Simple file serving
   python -m http.server 8000
   
   # Option 2: Live reload (requires Node.js)
   npx live-server --port=8080 --host=localhost
   ```
5. **Open the application** in your browser and start developing!

### Testing Your Changes
- **Test in multiple browsers**: Chrome, Firefox, Safari, Edge
- **Test on different devices**: Desktop, tablet, mobile
- **Test different file types**: Images, PDFs, text files, etc.
- **Test security features**: Password protection, encryption/decryption
- **Test edge cases**: Large files, special characters, network issues

## 📋 Development Guidelines

### Code Style
- **Follow existing code style** and patterns
- **Use meaningful variable names** and function names
- **Add comments** for complex logic
- **Keep functions small** and focused
- **Use modern JavaScript features** (ES6+)

### Security First
- **Never compromise security** for convenience
- **Review cryptographic implementations** carefully
- **Use Web Crypto API** for all cryptographic operations
- **Validate user input** thoroughly
- **Consider timing attacks** and side-channel vulnerabilities

### Architecture Principles
- **Maintain single-file architecture** for simplicity
- **Keep client-side focus** - no server-side dependencies
- **Ensure mobile responsiveness**
- **Optimize for performance**
- **Handle errors gracefully**

### HTML Structure
```html
<!-- Follow this structure for new sections -->
<div class="section-container">
    <h2 class="section-title">Section Title</h2>
    <div class="section-content">
        <!-- Content here -->
    </div>
</div>
```

### CSS Guidelines
- **Use CSS Grid** and Flexbox for layouts
- **Follow BEM methodology** for class naming
- **Maintain dark theme consistency**
- **Use CSS custom properties** for theming
- **Ensure accessibility** with proper focus states

### JavaScript Patterns
```javascript
// Use modern async/await
async function encryptFile(file, key) {
    try {
        // Implementation
    } catch (error) {
        console.error('Encryption failed:', error);
        throw error;
    }
}

// Use proper error handling
function handleError(error, context) {
    console.error(`Error in ${context}:`, error);
    showNotification('error', 'Operation failed. Please try again.');
}
```

## 🔍 Pull Request Process

### Before Submitting
1. **Test thoroughly** in multiple browsers
2. **Check for console errors** and warnings
3. **Verify security implications** of your changes
4. **Update documentation** if needed
5. **Ensure code follows style guidelines**

### Pull Request Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Security enhancement

## Testing
- [ ] Tested in Chrome
- [ ] Tested in Firefox
- [ ] Tested in Safari
- [ ] Tested on mobile
- [ ] Tested with different file types

## Security Impact
Describe any security implications of your changes.

## Screenshots (if applicable)
Add screenshots or recordings of your changes.
```

### Review Process
1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Security review** for sensitive changes
4. **Testing** in different environments
5. **Approval** and merge

## 🐛 Bug Report Template

When reporting bugs, please include:

```markdown
**Bug Description**
A clear description of what the bug is.

**Steps to Reproduce**
1. Go to '...'
2. Click on '....'
3. Upload file '....'
4. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- Browser: [e.g., Chrome 96]
- OS: [e.g., Windows 10]
- Device: [e.g., Desktop, iPhone 12]

**Console Errors**
Any error messages from browser console.

**Additional Context**
Any other relevant information.
```

## 💡 Feature Request Template

```markdown
**Feature Description**
Clear description of the feature you'd like to see.

**Problem Statement**
What problem does this feature solve?

**Proposed Solution**
How would you like this feature to work?

**Alternatives Considered**
Other solutions you've considered.

**Use Cases**
Specific scenarios where this would be useful.

**Security Considerations**
Any security implications to consider.
```

## 🔒 Security Guidelines

### Reporting Security Issues
- **Do not** report security vulnerabilities in public issues
- **Email security concerns** to: [security@example.com]
- **Provide detailed information** about the vulnerability
- **Allow time** for fixes before public disclosure

### Security Review Checklist
- [ ] No sensitive data in logs
- [ ] Proper input validation
- [ ] Secure random number generation
- [ ] Correct cryptographic implementations
- [ ] No timing attack vulnerabilities
- [ ] Proper error handling without information leakage

## 📚 Resources

### Documentation
- [Web Crypto API MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API)
- [File API MDN](https://developer.mozilla.org/en-US/docs/Web/API/File)
- [Progressive Web Apps](https://web.dev/progressive-web-apps/)

### Cryptography
- [RFC 3394 - AES Key Wrap](https://tools.ietf.org/html/rfc3394)
- [RFC 2898 - PKCS #5: PBKDF2](https://tools.ietf.org/html/rfc2898)
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

### Browser APIs
- [Web Share API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Share_API)
- [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API)
- [Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)

## 🎯 Project Roadmap

### Current Focus
- [ ] Improve mobile experience
- [ ] Add batch operations
- [ ] Enhance accessibility
- [ ] Performance optimizations

### Future Plans
- [ ] Progressive Web App features
- [ ] Offline functionality
- [ ] Multi-language support
- [ ] Advanced file management

## 📞 Community

### Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Discord**: Real-time chat (if applicable)
- **Email**: Security and private matters

### Code of Conduct
- **Be respectful** and inclusive
- **Focus on constructive feedback**
- **Help others** learn and grow
- **Maintain professionalism**
- **Respect different perspectives**

## 🏆 Recognition

Contributors are recognized in:
- **README.md** acknowledgments section
- **Release notes** for significant contributions
- **Contributors** section on GitHub
- **Special thanks** for security improvements

## 📝 License

By contributing to Rahastra, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

**Thank you for contributing to Rahastra! Your help makes secure file sharing accessible to everyone.**