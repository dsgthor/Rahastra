# Pull Request Template

Create this file as `.github/pull_request_template.md`:

```markdown
# Pull Request

## 📝 Description
<!-- Provide a brief description of the changes in this PR -->

Briefly describe what this PR does and why it's needed.

## 🔗 Related Issues
<!-- Link to any related issues using GitHub's closing keywords -->
<!-- Example: Closes #123, Fixes #456, Resolves #789 -->

- Closes # (issue number)

## 🔄 Type of Change
<!-- Mark the relevant option with an [x] -->

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update (changes to documentation only)
- [ ] 🔧 Refactoring (code changes that neither fix a bug nor add a feature)
- [ ] ⚡ Performance improvement
- [ ] 🧪 Test addition or improvement
- [ ] 🔒 Security improvement
- [ ] 🎨 UI/UX improvement
- [ ] 🔨 Build/CI changes

## 🧪 Testing
<!-- Describe the tests you ran and how to reproduce them -->

### Test Environment
- [ ] Local development environment
- [ ] HTTP mode
- [ ] HTTPS mode (self-signed certificate)
- [ ] HTTPS mode (valid certificate)

### Browser Testing
<!-- Mark all browsers you've tested on -->
- [ ] Chrome (version: ______)
- [ ] Firefox (version: ______)
- [ ] Safari (version: ______)
- [ ] Edge (version: ______)
- [ ] Mobile Chrome
- [ ] Mobile Safari

### Device Testing
- [ ] Desktop (Windows)
- [ ] Desktop (macOS)
- [ ] Desktop (Linux)
- [ ] Mobile (Android)
- [ ] Mobile (iOS)
- [ ] Tablet

### Feature Testing
<!-- Mark relevant tests you've performed -->
- [ ] File upload/download works correctly
- [ ] Multiple file selection works
- [ ] Large file transfers (>100MB) work
- [ ] Password-protected rooms work
- [ ] QR code generation/scanning works
- [ ] Connection handling works properly
- [ ] Error handling works as expected
- [ ] UI is responsive and accessible

### Test Cases
<!-- Describe specific test cases you ran -->
```
1. Test case description
   - Steps: 
   - Expected result: 
   - Actual result: 

2. Test case description
   - Steps: 
   - Expected result: 
   - Actual result: 
```

## 📱 Screenshots
<!-- Add screenshots for UI changes -->
<!-- Use the format: ![Description](image-url) or drag and drop images -->

### Before
<!-- Screenshot of the current state -->

### After
<!-- Screenshot of the changes -->

## 🔍 Code Quality
<!-- Mark completed items with [x] -->

### Code Review Checklist
- [ ] Code follows the project's style guidelines
- [ ] Self-review of code has been performed
- [ ] Code is well-commented, particularly in hard-to-understand areas
- [ ] No console.log statements left in production code
- [ ] No debugging code left in the PR
- [ ] Variable names are descriptive and follow conventions
- [ ] Functions are reasonably sized and focused
- [ ] Error handling is implemented where appropriate

### Security Checklist
- [ ] No hardcoded credentials or sensitive information
- [ ] Input validation is implemented where needed
- [ ] No new security vulnerabilities introduced
- [ ] HTTPS compatibility maintained
- [ ] No unsafe innerHTML or eval usage

### Performance Checklist
- [ ] No obvious performance regressions
- [ ] Large file handling is efficient
- [ ] Memory usage is reasonable
- [ ] No unnecessary network requests
- [ ] Code is optimized for mobile devices

## 📚 Documentation
<!-- Mark completed items with [x] -->

- [ ] README.md updated (if needed)
- [ ] Code comments added/updated
- [ ] API documentation updated (if applicable)
- [ ] Configuration documentation updated (if applicable)
- [ ] Troubleshooting guide updated (if applicable)

## ⚠️ Breaking Changes
<!-- If this is a breaking change, describe what changes users need to make -->

This PR introduces breaking changes:
- [ ] Yes (describe below)
- [ ] No

### Migration Guide
<!-- If breaking changes exist, provide migration instructions -->
```
// Example of changes needed:
// Old way:
// New way:
```

## 🔧 Configuration Changes
<!-- If this PR requires configuration changes -->

- [ ] No configuration changes required
- [ ] New configuration options added (backward compatible)
- [ ] Existing configuration options modified
- [ ] Configuration file format changed

### New Configuration Options
```python
# Example of new configuration options
--new-option: Description of what this option does
```

## 🚀 Deployment Notes
<!-- Any special deployment considerations -->

- [ ] No special deployment steps required
- [ ] Requires server restart
- [ ] Requires database migration
- [ ] Requires new dependencies
- [ ] Requires environment variable changes

### Deployment Steps
```bash
# If special deployment steps are needed:
1. Step 1
2. Step 2
3. Step 3
```

## 🧩 Dependencies
<!-- Mark if this PR adds, updates, or removes dependencies -->

- [ ] No dependency changes
- [ ] Added new dependencies
- [ ] Updated existing dependencies
- [ ] Removed dependencies

### Dependency Changes
```txt
# Added:
new-package==1.0.0

# Updated:
existing-package==1.2.0 -> 2.0.0

# Removed:
old-package==0.5.0
```

## 🔮 Future Considerations
<!-- Any thoughts on future improvements or considerations -->

This PR sets up for future improvements:
- [ ] Enables new features to be built on top
- [ ] Improves code maintainability
- [ ] Improves test coverage
- [ ] Improves documentation

## ✅ Final Checklist
<!-- Complete this checklist before requesting review -->

- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## 🤝 Reviewer Notes
<!-- Any specific notes for reviewers -->

Please pay special attention to:
- [ ] Security implications
- [ ] Performance impact
- [ ] Mobile compatibility
- [ ] Accessibility features
- [ ] Error handling
- [ ] Browser compatibility

## 📝 Additional Notes
<!-- Any additional information that reviewers should know -->

---

### For Maintainers

**Merge Checklist:**
- [ ] All CI checks pass
- [ ] Code review completed
- [ ] Documentation updated
- [ ] Version bumped (if needed)
- [ ] Changelog updated
- [ ] Security review completed (if applicable)

**Post-Merge:**
- [ ] Deploy to staging
- [ ] Test on staging
- [ ] Deploy to production (if applicable)
- [ ] Monitor for issues
- [ ] Update project board
```