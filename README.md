# Crime Data Analysis of Ontario Cities (2021-2024)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

A comprehensive data analysis project examining crime trends across major Ontario cities from 2021 to 2024, utilizing statistical analysis, machine learning, and time series forecasting techniques.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🎯 Project Overview

This project analyzes crime rates across five major Ontario cities (Toronto, Windsor, Guelph, London, and Kitchener-Waterloo-Cambridge) from 2021 to 2024. Using publicly available statistics from Statistics Canada, the analysis aims to:

- Identify crime patterns and trends
- Discover city-level differences
- Predict future crime trends using statistical and machine learning methods
- Support evidence-based decision-making for policing and urban planning

**Course:** INFO8126 - Data Acquisition, Analysis and Visualization  
**Institution:** Conestoga College, Institute of Technology and Advanced Learning  
**Professor:** Maggie Santos

---

## 📊 Dataset

**Source:** [Statistics Canada - Incident-based crime statistics](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)

**File:** `Crime Dataset for Data Acquisition.csv`

**Variables:**
| Variable | Description |
|----------|-------------|
| `REF_DATE` | Year of incident (2021-2024) |
| `GEO` | Geographic location/city |
| `Violations` | Type of crime/violation |
| `Statistics` | Statistical measure type |
| `VALUE` | Crime count or rate |

**Cities Analyzed:**
- Toronto
- Windsor
- Guelph
- London
- Kitchener-Waterloo-Cambridge

**Time Period:** 2021-2024

---

## 🔬 Methodology

### 1. Data Cleaning & Preparation
- Filtered for "Actual incidents" only
- Handled missing values
- Standardized data types
- Applied one-hot encoding for categorical variables
- Renamed columns for clarity (Year, City, Violations, Value)

### 2. Exploratory Data Analysis (EDA)
- Descriptive statistics by violation type
- Distribution analysis
- City-wise comparisons

### 3. Data Visualization
- Horizontal bar charts (Total Crime by City)
- Boxplots (Distribution by Violation Type)
- Heatmaps (Crime Values by City and Year)

### 4. Descriptive Data Mining
- **K-Means Clustering** to segment cities based on crime profiles
- **PCA** for dimensionality reduction and visualization

### 5. Statistical Inference
- **Independent Samples t-Test** comparing Toronto vs Windsor crime levels
- Hypothesis testing to validate significance of differences

### 6. Predictive Modeling
- **Linear Regression** (baseline model)
- **Random Forest Regression** (ensemble method)
- Performance comparison using R² and RMSE

### 7. Time Series Forecasting
- **Exponential Smoothing** for trend analysis
- Crime forecast for 2025

---

## 🔑 Key Findings

### Crime Volume by City
| City | Crime Level | Total Incidents (2021-2024) |
|------|-------------|----------------------------|
| **Toronto** | 🔴 High-Risk | > 2.4 million |
| **London** | 🟡 Moderate | Mid-range |
| **Kitchener-Waterloo** | 🟡 Moderate | Mid-range |
| **Windsor** | 🟢 Low-Risk | Low |
| **Guelph** | 🟢 Low-Risk | Lowest |

### Most Common Violations
1. **Assault, Level 1** - Highest average (6,137 incidents)
2. **Sexual Assault** - ~1,000+ average incidents
3. **Robbery** - ~1,000+ average incidents
4. **Impaired Driving** - High variability
5. **Drug Violations** - Significant contributor

### Statistical Test Results
- **t-statistic:** 2.1115
- **p-value:** 0.0329 (< 0.05)
- **Conclusion:** Statistically significant difference between Toronto and Windsor crime levels

### Model Performance
| Model | R² Score | RMSE | Performance |
|-------|----------|------|-------------|
| Linear Regression | -96.01 | 14,951 | ❌ Poor |
| Random Forest | 0.944 | 360.43 | ✅ Excellent |

### 2025 Forecast
- **Predicted Total Crimes:** ~504,272 incidents
- **Trend:** Continued year-over-year increase

---

## 💻 Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

### Python Libraries
```
pandas >= 1.3.0
numpy >= 1.21.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
scikit-learn >= 0.24.0
statsmodels >= 0.12.0
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/crime-data-analysis-ontario.git
   cd crime-data-analysis-ontario
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

---

## 🚀 Usage

### Running the Analysis

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook Crime_Data_Analysis.ipynb
   ```

2. Run all cells sequentially to reproduce the analysis

3. Key notebook sections:
   - **Section 1:** Data Loading and Cleaning
   - **Section 2:** Exploratory Data Analysis
   - **Section 3:** Data Visualization
   - **Section 4:** Clustering Analysis
   - **Section 5:** Statistical Inference
   - **Section 6:** Predictive Modeling
   - **Section 7:** Time Series Forecasting

### Customizing the Analysis

To analyze different cities or time periods:

```python
# Filter for specific cities
cities_of_interest = ['Toronto', 'Ottawa', 'Hamilton']
filtered_data = df[df['City'].isin(cities_of_interest)]

# Filter for specific years
year_range = df[(df['Year'] >= 2020) & (df['Year'] <= 2024)]
```

---

## 📁 Project Structure

```
crime-data-analysis-ontario/
│
├── 📄 README.md                          # Project documentation
├── 📄 LICENSE                            # MIT License
├── 📄 requirements.txt                   # Python dependencies
├── 📄 CONTRIBUTING.md                    # Contribution guidelines
├── 📄 CODE_OF_CONDUCT.md                 # Community standards
├── 📄 .gitignore                         # Git ignore rules
│
├── 📊 Crime Dataset for Data Acquisition.csv   # Raw dataset
├── 📓 Crime_Data_Analysis.ipynb          # Main Jupyter notebook
│
├── 📁 docs/                              # Additional documentation
│   ├── Group_Project_Report.pdf          # Full project report
│   ├── Data_Acquisition_Presentation.pptx # Project presentation
│   └── methodology.md                    # Detailed methodology
│
└── 📁 src/                               # Source code (if modularized)
    ├── data_cleaning.py
    ├── visualization.py
    ├── clustering.py
    ├── statistical_tests.py
    └── forecasting.py
```

---

## 📈 Results

### Clustering Results
Three distinct city clusters identified:
- **Cluster 1 (High-Risk):** Toronto
- **Cluster 0 (Moderate-Risk):** London, Kitchener-Waterloo
- **Cluster 2 (Low-Risk):** Guelph, Windsor

### Model Comparison
![Model Performance](outputs/figures/model_comparison.png)

### Crime Trend Forecast
![Time Series Forecast](outputs/figures/forecast_2025.png)

---

## 👥 Contributors

| Name | Role | Contribution |
|------|------|--------------|
| **Sakshi Sandeep Salvi** | Data Collection & Cleaning, Report Writing | R/A |
| **Mitali Sharma** | EDA, Data Visualization, PowerPoint | R/A |
| **Nitigya Vasudev** | Data Visualization, Clustering | R/C |
| **Umang Sehgal** | Statistical Inference, Regression | R/A |
| **Prince Choudhary** | Time Series Forecasting, Final Review | R/A |

**Legend:** R = Responsible | A = Accountable | C = Consulted | I = Informed

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Professor Maggie Santos** for guidance and supervision
- **Statistics Canada** for providing the crime data
- **Conestoga College** for academic support
- **Scikit-learn, Pandas, and Matplotlib** communities for excellent documentation

---

## 🔗 Related Resources

- [Statistics Canada Crime Statistics](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)
- [Project Report (PDF)](docs/Group_Project_Report.pdf)
- [Presentation (PPTX)](docs/Data_Acquisition_Presentation.pptx)

---

<p align="center">
  <i>Data-driven insights for safer communities</i>
</p>

<p align="center">
  Made with ❤️ by Conestoga College Business Analytics Students
</p>
