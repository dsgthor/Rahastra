# GitHub Issue Templates

Create these files in `.github/ISSUE_TEMPLATE/` directory:

## 1. Bug Report Template
**File: `.github/ISSUE_TEMPLATE/bug_report.yml`**

```yaml
name: 🐛 Bug Report
description: Report a bug or issue with DirectDrop Lite
title: "[BUG] "
labels: ["bug", "triage"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to report a bug! Please fill out the information below to help us diagnose the issue.

  - type: textarea
    id: bug-description
    attributes:
      label: Bug Description
      description: A clear and concise description of what the bug is.
      placeholder: Describe the bug...
    validations:
      required: true

  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Steps to Reproduce
      description: Steps to reproduce the behavior
      placeholder: |
        1. Go to '...'
        2. Click on '...'
        3. Scroll down to '...'
        4. See error
    validations:
      required: true

  - type: textarea
    id: expected-behavior
    attributes:
      label: Expected Behavior
      description: A clear and concise description of what you expected to happen.
      placeholder: What should happen?
    validations:
      required: true

  - type: textarea
    id: actual-behavior
    attributes:
      label: Actual Behavior
      description: What actually happened?
      placeholder: What actually happened?
    validations:
      required: true

  - type: dropdown
    id: operating-system
    attributes:
      label: Operating System
      description: What operating system are you using?
      options:
        - Windows 10
        - Windows 11
        - macOS 12 (Monterey)
        - macOS 13 (Ventura)
        - macOS 14 (Sonoma)
        - Ubuntu 20.04
        - Ubuntu 22.04
        - Other Linux
        - Android
        - iOS
        - Other
    validations:
      required: true

  - type: dropdown
    id: browser
    attributes:
      label: Browser
      description: Which browser are you using?
      options:
        - Chrome
        - Firefox
        - Safari
        - Edge
        - Opera
        - Other
    validations:
      required: true

  - type: input
    id: browser-version
    attributes:
      label: Browser Version
      description: What version of the browser are you using?
      placeholder: e.g., 119.0.6045.105
    validations:
      required: true

  - type: input
    id: python-version
    attributes:
      label: Python Version
      description: What version of Python are you using?
      placeholder: e.g., 3.9.7
    validations:
      required: true

  - type: dropdown
    id: https-mode
    attributes:
      label: HTTPS Mode
      description: Were you using HTTP or HTTPS?
      options:
        - HTTP
        - HTTPS (self-signed)
        - HTTPS (valid certificate)
    validations:
      required: true

  - type: textarea
    id: console-errors
    attributes:
      label: Console Errors
      description: Any errors in the browser console or Python output?
      placeholder: Paste any error messages here...
      render: shell

  - type: textarea
    id: screenshots
    attributes:
      label: Screenshots
      description: If applicable, add screenshots to help explain your problem.
      placeholder: Drag and drop images here or paste image URLs

  - type: textarea
    id: additional-context
    attributes:
      label: Additional Context
      description: Add any other context about the problem here.
      placeholder: Any additional information that might be helpful...

  - type: checkboxes
    id: checklist
    attributes:
      label: Checklist
      description: Please confirm the following
      options:
        - label: I have searched existing issues for duplicates
          required: true
        - label: I have provided all the requested information
          required: true
        - label: I have tested with the latest version
          required: true
```

## 2. Feature Request Template
**File: `.github/ISSUE_TEMPLATE/feature_request.yml`**

```yaml
name: ✨ Feature Request
description: Suggest a new feature or enhancement for DirectDrop Lite
title: "[FEATURE] "
labels: ["enhancement", "triage"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting a new feature! Please provide details about your request.

  - type: textarea
    id: feature-description
    attributes:
      label: Feature Description
      description: A clear and concise description of the feature you'd like to see
      placeholder: Describe the feature...
    validations:
      required: true

  - type: textarea
    id: problem-statement
    attributes:
      label: Problem Statement
      description: What problem does this feature solve? What need does it address?
      placeholder: This feature would solve...
    validations:
      required: true

  - type: textarea
    id: proposed-solution
    attributes:
      label: Proposed Solution
      description: How do you envision this feature working?
      placeholder: The feature should work by...
    validations:
      required: true

  - type: textarea
    id: use-cases
    attributes:
      label: Use Cases
      description: Provide specific examples of how this feature would be used
      placeholder: |
        1. As a user, I would...
        2. When I need to...
        3. This would help when...

  - type: textarea
    id: alternatives
    attributes:
      label: Alternative Solutions
      description: Have you considered any alternative approaches?
      placeholder: Other approaches I've considered...

  - type: dropdown
    id: priority
    attributes:
      label: Priority
      description: How important is this feature to you?
      options:
        - Low - Nice to have
        - Medium - Would be helpful
        - High - Important for my use case
        - Critical - Blocking current functionality
    validations:
      required: true

  - type: dropdown
    id: complexity
    attributes:
      label: Estimated Complexity
      description: How complex do you think this feature is to implement?
      options:
        - Simple - Minor change or addition
        - Medium - Moderate development effort
        - Complex - Significant development effort
        - Unknown - I'm not sure

  - type: checkboxes
    id: feature-type
    attributes:
      label: Feature Type
      description: What type of feature is this? (Select all that apply)
      options:
        - label: User Interface improvement
        - label: File transfer enhancement
        - label: Security feature
        - label: Performance optimization
        - label: Mobile compatibility
        - label: Accessibility improvement
        - label: Developer experience
        - label: Documentation improvement

  - type: textarea
    id: mockups
    attributes:
      label: Mockups or Examples
      description: If applicable, add mockups, wireframes, or examples from other applications
      placeholder: Add images or links to examples...

  - type: textarea
    id: additional-context
    attributes:
      label: Additional Context
      description: Any other information that would be helpful
      placeholder: Additional context...

  - type: checkboxes
    id: checklist
    attributes:
      label: Checklist
      description: Please confirm the following
      options:
        - label: I have searched existing issues for similar requests
          required: true
        - label: This feature aligns with the project's goals
          required: true
        - label: I would be willing to help test this feature
```

## 3. Question Template
**File: `.github/ISSUE_TEMPLATE/question.yml`**

```yaml
name: ❓ Question
description: Ask a question about DirectDrop Lite
title: "[QUESTION] "
labels: ["question", "triage"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Have a question about DirectDrop Lite? We're here to help!
        
        💡 **Tip:** Check the [documentation](https://github.com/yourusername/directdrop-lite/blob/main/README.md) and [existing issues](https://github.com/yourusername/directdrop-lite/issues) first.

  - type: textarea
    id: question
    attributes:
      label: Your Question
      description: What would you like to know?
      placeholder: Ask your question here...
    validations:
      required: true

  - type: dropdown
    id: category
    attributes:
      label: Question Category
      description: What is your question about?
      options:
        - Installation and Setup
        - Configuration
        - Usage and Features
        - Troubleshooting
        - Security
        - Performance
        - Development
        - Deployment
        - Other
    validations:
      required: true

  - type: textarea
    id: context
    attributes:
      label: Context
      description: Provide any relevant context (what you're trying to do, your setup, etc.)
      placeholder: I'm trying to...

  - type: textarea
    id: what-tried
    attributes:
      label: What Have You Tried?
      description: Have you tried anything to solve this yourself?
      placeholder: I have tried...

  - type: input
    id: environment
    attributes:
      label: Environment
      description: Your setup (OS, Python version, browser, etc.)
      placeholder: e.g., Windows 10, Python 3.9, Chrome 119

  - type: checkboxes
    id: checklist
    attributes:
      label: Checklist
      description: Please confirm the following
      options:
        - label: I have read the documentation
          required: true
        - label: I have searched existing issues
          required: true
```

## 4. Performance Issue Template
**File: `.github/ISSUE_TEMPLATE/performance.yml`**

```yaml
name: 🐌 Performance Issue
description: Report a performance problem with DirectDrop Lite
title: "[PERFORMANCE] "
labels: ["performance", "triage"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Thanks for reporting a performance issue! Performance data helps us improve DirectDrop Lite for everyone.

  - type: textarea
    id: performance-issue
    attributes:
      label: Performance Issue Description
      description: Describe the performance problem you're experiencing
      placeholder: The application is slow when...
    validations:
      required: true

  - type: dropdown
    id: issue-type
    attributes:
      label: Issue Type
      description: What type of performance issue is this?
      options:
        - Slow file transfer
        - High memory usage
        - High CPU usage
        - Slow UI response
        - Connection delays
        - Browser freezing
        - Other
    validations:
      required: true

  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Steps to Reproduce
      description: How can we reproduce this performance issue?
      placeholder: |
        1. Start the application with...
        2. Transfer a file of size...
        3. Notice the slowdown when...
    validations:
      required: true

  - type: input
    id: file-size
    attributes:
      label: File Size
      description: What size files are you transferring?
      placeholder: e.g., 100MB, 1GB, 5GB

  - type: input
    id: network-speed
    attributes:
      label: Network Speed
      description: What's your network speed (upload/download)?
      placeholder: e.g., 100 Mbps download, 50 Mbps upload

  - type: dropdown
    id: device-type
    attributes:
      label: Device Type
      description: What type of device are you using?
      options:
        - Desktop (High-end)
        - Desktop (Mid-range)
        - Desktop (Low-end)
        - Laptop (High-end)
        - Laptop (Mid-range)
        - Laptop (Low-end)
        - Tablet
        - Mobile Phone
    validations:
      required: true

  - type: textarea
    id: system-specs
    attributes:
      label: System Specifications
      description: Your system specs (CPU, RAM, etc.)
      placeholder: |
        CPU: Intel i7-10700K
        RAM: 16GB
        Storage: SSD
        OS: Windows 10

  - type: textarea
    id: performance-metrics
    attributes:
      label: Performance Metrics
      description: Any specific metrics you've observed (transfer speeds, memory usage, etc.)
      placeholder: |
        Transfer speed: 5 MB/s (expected 50 MB/s)
        Memory usage: 2GB (seems high)
        CPU usage: 80% during transfer

  - type: textarea
    id: browser-performance
    attributes:
      label: Browser Performance Tools
      description: Any insights from browser dev tools (Performance tab, Memory tab, etc.)
      placeholder: Browser dev tools show...

  - type: checkboxes
    id: checklist
    attributes:
      label: Checklist
      description: Please confirm the following
      options:
        - label: I have tested with the latest version
          required: true
        - label: I have closed other applications to isolate the issue
          required: true
        - label: The issue is reproducible
          required: true
```

## 5. Config Template
**File: `.github/ISSUE_TEMPLATE/config.yml`**

```yaml
blank_issues_enabled: false
contact_links:
  - name: 💬 GitHub Discussions
    url: https://github.com/yourusername/directdrop-lite/discussions
    about: Ask questions and discuss with the community
  - name: 📚 Documentation
    url: https://github.com/yourusername/directdrop-lite/blob/main/README.md
    about: Check the documentation for guides and examples
  - name: 🔒 Security Issues
    url: mailto:security@directdrop.example.com
    about: Report security vulnerabilities privately
```

---

These templates will help organize and standardize issue reporting, making it easier for maintainers to understand and address problems quickly. Each template is designed to gather the specific information needed for that type of issue.