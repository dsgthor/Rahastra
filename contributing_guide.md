# Contributing to DirectDrop Lite

Thank you for your interest in contributing to DirectDrop Lite! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue templates** when creating new issues
3. **Provide detailed information** including:
   - Operating system and version
   - Browser and version
   - Python version
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Screenshots or error messages

### Suggesting Features

1. Open a **Feature Request** issue
2. Describe the feature and its benefits
3. Provide use cases and examples
4. Consider the impact on existing functionality

### Code Contributions

#### Prerequisites

- Python 3.8 or higher
- Git installed and configured
- Basic understanding of FastAPI and WebRTC
- Familiarity with modern JavaScript (ES6+)

#### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/directdrop-lite.git
   cd directdrop-lite
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Run the application**
   ```bash
   python directdrop_lite2.py --https
   ```

#### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make your changes**
   - Follow the coding standards (see below)
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   - Test on multiple browsers (Chrome, Firefox, Safari, Edge)
   - Test both HTTP and HTTPS modes
   - Test file transfers of various sizes
   - Verify mobile compatibility

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

5. **Push and create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 📋 Coding Standards

### Python Code

- Follow **PEP 8** style guidelines
- Use **type hints** where appropriate
- Maximum line length: **88 characters** (Black formatter)
- Use **descriptive variable names**
- Add **docstrings** for functions and classes

Example:
```python
async def create_room(room_code: str, password: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new room for file transfer.
    
    Args:
        room_code: Unique identifier for the room
        password: Optional password for room access
        
    Returns:
        Dictionary containing room information
    """
```

### JavaScript Code

- Use **ES6+ syntax** (const/let, arrow functions, async/await)
- Use **camelCase** for variables and functions
- Use **PascalCase** for classes
- Add **JSDoc comments** for complex functions
- Maximum line length: **100 characters**

Example:
```javascript
/**
 * Handles file transfer progress updates
 * @param {number} progress - Progress percentage (0-100)
 * @param {string} fileName - Name of the file being transferred
 */
const updateProgress = (progress, fileName) => {
    // Implementation
};
```

### HTML/CSS

- Use **semantic HTML** elements
- Follow **BEM methodology** for CSS classes
- Use **CSS custom properties** for theming
- Ensure **accessibility** (ARIA labels, keyboard navigation)

## 🧪 Testing Guidelines

### Manual Testing Checklist

- [ ] File transfer works on different browsers
- [ ] HTTPS mode functions correctly
- [ ] QR code generation and scanning
- [ ] Mobile device compatibility
- [ ] Large file handling (>100MB)
- [ ] Multiple file selection and transfer
- [ ] Connection error handling
- [ ] Password-protected rooms

### Browser Testing Matrix

| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | 80+     | ✅ Primary |
| Firefox | 75+     | ✅ Primary |
| Safari  | 13+     | ✅ Primary |
| Edge    | 80+     | ✅ Primary |

## 📝 Documentation

### Code Documentation

- **Docstrings**: All public functions and classes
- **Inline comments**: Complex logic and algorithms
- **Type hints**: Function parameters and return types
- **README updates**: New features and configuration options

### User Documentation

- Update **README.md** for new features
- Add **usage examples** for new functionality
- Update **troubleshooting** section for known issues
- Create **FAQ entries** for common questions

## 🔄 Pull Request Process

### Before Submitting

1. **Rebase** your branch on the latest main
2. **Squash** related commits into logical units
3. **Test** thoroughly on multiple browsers
4. **Update** documentation and changelog
5. **Run** linting and formatting tools

### PR Title Format

Use conventional commit format:
- `feat: add new feature`
- `fix: resolve issue with file transfer`
- `docs: update installation guide`
- `refactor: improve code organization`
- `test: add browser compatibility tests`

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested on Chrome
- [ ] Tested on Firefox
- [ ] Tested on Safari
- [ ] Tested on mobile devices
- [ ] Tested with HTTPS
- [ ] Tested large file transfers

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

### Review Process

1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Testing** on different environments
4. **Approval** required before merge

## 🐛 Bug Reports

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Windows 10, macOS 11.2]
- Browser: [e.g., Chrome 95, Firefox 94]
- Python Version: [e.g., 3.9.7]
- Application Version: [e.g., v1.0.0]

**Additional Context**
Screenshots, error logs, etc.
```

## 🚀 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Problem Statement**
What problem does this solve?

**Proposed Solution**
How should this feature work?

**Alternative Solutions**
Other approaches considered

**Additional Context**
Mockups, examples, references
```

## 📦 Release Process

### Version Numbering

Follow **Semantic Versioning** (SemVer):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Create release notes
- [ ] Tag the release
- [ ] Test release build

## 🏆 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub Discussions** for community highlights

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and community chat
- **Email**: [maintainer@email.com] for private inquiries

## 🎯 Priorities

Current focus areas:
1. **Mobile compatibility** improvements
2. **Large file transfer** optimization
3. **Security** enhancements
4. **Accessibility** improvements
5. **Documentation** expansion

Thank you for contributing to DirectDrop Lite! 🚀