# Setup Guide

## Crime Data Analysis Project - Quick Start

---

## Prerequisites

Before you begin, ensure you have:
- [ ] Python 3.8 or higher installed
- [ ] pip package manager
- [ ] Git (for cloning)
- [ ] 2GB free disk space
- [ ] Internet connection (for downloading packages)

---

## Quick Start (5 minutes)

### Option 1: Using pip

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/crime-data-analysis-ontario.git
cd crime-data-analysis-ontario

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Launch Jupyter
jupyter notebook
```

### Option 2: Using Conda

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/crime-data-analysis-ontario.git
cd crime-data-analysis-ontario

# 2. Create conda environment
conda create -n crime-analysis python=3.9

# 3. Activate environment
conda activate crime-analysis

# 4. Install dependencies
pip install -r requirements.txt

# 5. Launch Jupyter
jupyter notebook
```

---

## Detailed Installation

### Step 1: Install Python

**Windows:**
1. Download from [python.org](https://python.org)
2. Run installer
3. Check "Add Python to PATH"
4. Click "Install Now"

**macOS:**
```bash
# Using Homebrew
brew install python

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 2: Verify Installation

```bash
python --version  # Should show 3.8+
pip --version
```

### Step 3: Clone Repository

```bash
git clone https://github.com/yourusername/crime-data-analysis-ontario.git
cd crime-data-analysis-ontario
```

### Step 4: Create Virtual Environment

**Why use virtual environments?**
- Isolates project dependencies
- Prevents version conflicts
- Makes project portable

```bash
# Create environment
python -m venv venv

# Activate
# Windows Command Prompt:
venv\Scripts\activate.bat

# Windows PowerShell:
venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate

# Verify (should show path to venv)
which python
```

### Step 5: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Installation may take 2-5 minutes.**

### Step 6: Verify Installation

```bash
python -c "import pandas; import sklearn; print('All packages installed successfully!')"
```

### Step 7: Launch Jupyter

```bash
jupyter notebook
```

This will open your browser at `http://localhost:8888`

---

## Running the Analysis

### Opening the Notebook

1. In Jupyter interface, click on `Crime_Data_Analysis.ipynb`
2. Wait for the notebook to load
3. You should see the notebook with code cells

### Running All Cells

**Option 1: Run all at once**
- Click `Cell` → `Run All`
- Wait for all cells to execute

**Option 2: Run step by step**
- Click first cell
- Press `Shift + Enter` to run and move to next cell
- Repeat for each cell

### Expected Runtime

| Section | Approximate Time |
|---------|-----------------|
| Data Loading | 10-30 seconds |
| Data Cleaning | 30-60 seconds |
| EDA & Visualization | 1-2 minutes |
| Clustering | 30-60 seconds |
| Statistical Tests | 10-20 seconds |
| Regression Models | 1-2 minutes |
| Time Series | 20-40 seconds |
| **Total** | **5-8 minutes** |

---

## Troubleshooting

### Issue: pip not found

**Solution:**
```bash
# Windows
python -m pip install --upgrade pip

# macOS/Linux
python3 -m pip install --upgrade pip
```

### Issue: Permission denied (macOS/Linux)

**Solution:**
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use sudo (not recommended)
sudo pip install -r requirements.txt
```

### Issue: Jupyter won't start

**Solution:**
```bash
# Reinstall jupyter
pip uninstall jupyter
pip install jupyter

# Or try jupyterlab
pip install jupyterlab
jupyter lab
```

### Issue: Import errors

**Solution:**
```bash
# Reinstall specific package
pip uninstall pandas
pip install pandas

# Or reinstall all
pip install -r requirements.txt --force-reinstall
```

### Issue: Kernel dies in Jupyter

**Solution:**
1. Restart kernel: `Kernel` → `Restart`
2. Clear output: `Cell` → `All Output` → `Clear`
3. Run cells one by one to identify problematic cell

---

## Environment Variables (Optional)

Create a `.env` file for configuration:

```bash
# .env file
DATA_PATH=./data
OUTPUT_PATH=./outputs
RANDOM_SEED=42
```

Load in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
data_path = os.getenv('DATA_PATH')
```

---

## Updating the Project

To get latest updates:

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade
```

---

## Uninstallation

To remove the project:

```bash
# Deactivate environment
deactivate

# Remove virtual environment
# Windows:
rmdir /s venv

# macOS/Linux:
rm -rf venv

# Remove project folder
cd ..
rm -rf crime-data-analysis-ontario
```

---

## Getting Help

If you encounter issues:

1. Check [Issues](../../issues) page
2. Review [Troubleshooting](#troubleshooting) section
3. Create a new issue with:
   - Error message
   - Operating system
   - Python version
   - Steps to reproduce

---

## Next Steps

After successful setup:

1. 📖 Read the [README](README.md)
2. 📊 Explore the Jupyter notebook
3. 📄 Review the [methodology](docs/methodology.md)
4. 🤝 Consider [contributing](CONTRIBUTING.md)

---

**Happy Analyzing! 🎉**
