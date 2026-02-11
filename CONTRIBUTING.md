# Contributing to Crime Data Analysis of Ontario Cities

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please:
- Check if the issue already exists
- Use the latest version of the code
- Collect information about the bug (error messages, screenshots)

**Bug Report Template:**
```markdown
**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two
3. ...

**Expected Behavior:**
What you expected to happen

**Actual Behavior:**
What actually happened

**Environment:**
- Python version:
- OS:
- Package versions:
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Please:
- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Explain why this enhancement would be useful

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## 🛠️ Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment tool (venv, conda, etc.)

### Setup Steps

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/crime-data-analysis-ontario.git
cd crime-data-analysis-ontario

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install pytest black flake8
```

---

## 📝 Style Guidelines

### Python Code Style

We follow [PEP 8](https://pep8.org/) style guidelines:

```python
# Good example
def calculate_crime_rate(total_crimes, population):
    """Calculate crime rate per 100,000 population.
    
    Args:
        total_crimes (int): Total number of crimes
        population (int): Population count
        
    Returns:
        float: Crime rate per 100,000 population
    """
    if population == 0:
        return 0
    return (total_crimes / population) * 100000

# Bad example
def calcRate(x,y):
    return (x/y)*100000
```

### Jupyter Notebook Guidelines

- Keep cells focused on single operations
- Add markdown explanations between code cells
- Clear all outputs before committing
- Use meaningful variable names

### Documentation

- Add docstrings to all functions
- Include type hints where appropriate
- Update README.md if adding new features

---

## 💬 Commit Messages

Use clear and meaningful commit messages:

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semi colons, etc)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat: Add Random Forest model for crime prediction

Implement Random Forest regression with hyperparameter tuning.
Achieves R² = 0.94 on test data.

fix: Handle missing values in VALUE column

docs: Update README with installation instructions
```

---

## 🔄 Pull Request Process

1. **Before Submitting:**
   - Ensure code follows style guidelines
   - Add/update documentation as needed
   - Test your changes thoroughly
   - Update README.md if necessary

2. **PR Description Should Include:**
   - Description of changes
   - Motivation for changes
   - Screenshots (if applicable)
   - Testing performed

3. **Review Process:**
   - Maintainers will review your PR
   - Address any requested changes
   - Once approved, your PR will be merged

4. **After Merge:**
   - Your contribution will be acknowledged
   - Feel free to delete your branch

---

## 🏷️ Issue Labels

| Label | Description |
|-------|-------------|
| `bug` | Something isn't working |
| `enhancement` | New feature or request |
| `documentation` | Documentation improvements |
| `good first issue` | Good for newcomers |
| `help wanted` | Extra attention needed |
| `question` | Further information requested |

---

## 📚 Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [PEP 8 Style Guide](https://pep8.org/)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/en/latest/format.html)

---

## ❓ Questions?

Feel free to:
- Open an issue for questions
- Contact the project maintainers
- Check existing documentation

Thank you for contributing! 🎉
