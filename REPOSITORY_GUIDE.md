# Repository Guide

## Crime Data Analysis of Ontario Cities (2021-2024)

This guide provides an overview of all files in this repository and their purposes.

---

## 📁 Repository Structure

```
crime-data-analysis-ontario/
│
├── 📄 README.md                          ← Start here! Main project documentation
├── 📄 LICENSE                            ← MIT License
├── 📄 requirements.txt                   ← Python dependencies
├── 📄 CONTRIBUTING.md                    ← How to contribute
├── 📄 CODE_OF_CONDUCT.md                 ← Community guidelines
├── 📄 SETUP.md                           ← Installation instructions
├── 📄 .gitignore                         ← Git ignore rules
├── 📄 REPOSITORY_GUIDE.md                ← This file
│
├── 📊 Crime Dataset for Data Acquisition.csv   ← Your dataset (add this)
├── 📓 Crime_Data_Analysis.ipynb          ← Your Jupyter notebook (add this)
│
├── 📁 docs/                              ← Documentation folder
│   ├── Group_Project_Report.pdf          ← Full project report (add your PDF)
│   ├── Data_Acquisition_Presentation.pptx ← Project presentation (add your PPTX)
│   ├── methodology.md                    ← Detailed methodology
│   └── DATA_DICTIONARY.md                ← Data dictionary
│
├── 📁 outputs/                           ← Generated outputs
│   ├── figures/                          ← Save visualizations here
│   ├── tables/                           ← Save data tables here
│   └── models/                           ← Save trained models here
│
└── 📁 src/                               ← Source code modules
    ├── __init__.py                       ← Package initialization
    ├── data_cleaning.py                  ← Data preprocessing
    ├── visualization.py                  ← Plotting functions
    ├── clustering.py                     ← K-means clustering
    ├── statistical_tests.py              ← T-tests and ANOVA
    └── forecasting.py                    ← Time series forecasting
```

---

## 📋 File Descriptions

### Core Documentation

| File | Purpose | Read This If... |
|------|---------|-----------------|
| **README.md** | Main project overview | You want to understand the project |
| **SETUP.md** | Installation instructions | You need to set up the project |
| **CONTRIBUTING.md** | Contribution guidelines | You want to contribute |
| **CODE_OF_CONDUCT.md** | Community standards | You want to know our values |
| **LICENSE** | MIT License | You want to know usage rights |

### Data & Analysis

| File | Purpose | Status |
|------|---------|--------|
| **Crime Dataset for Data Acquisition.csv** | Raw data file | ⚠️ You need to add this |
| **Crime_Data_Analysis.ipynb** | Main Jupyter notebook | ⚠️ You need to add this |

### Documentation Folder (`docs/`)

| File | Purpose |
|------|---------|
| **methodology.md** | Detailed explanation of all analysis techniques |
| **DATA_DICTIONARY.md** | Complete variable descriptions |
| **Group_Project_Report.pdf** | Full academic report | ⚠️ Add your PDF |
| **Data_Acquisition_Presentation.pptx** | Project presentation | ⚠️ Add your PPTX |

### Source Code (`src/`)

| File | Purpose | Functions |
|------|---------|-----------|
| **data_cleaning.py** | Data preprocessing | `load_data()`, `clean_data()`, `handle_missing_values()` |
| **visualization.py** | Create charts | `plot_crime_by_city()`, `plot_heatmap()`, `plot_time_series()` |
| **clustering.py** | K-means analysis | `perform_clustering()`, `plot_clusters()`, `get_cluster_profiles()` |
| **statistical_tests.py** | Hypothesis testing | `perform_ttest()`, `perform_anova()`, `levene_test()` |
| **forecasting.py** | Time series | `fit_exponential_smoothing()`, `forecast_crimes()` |

---

## 🚀 Quick Start Checklist

### For Repository Setup:

- [ ] Copy your `Crime Dataset for Data Acquisition.csv` to root folder
- [ ] Copy your Jupyter notebook (`.ipynb`) to root folder
- [ ] Copy your `Group Project.pdf` to `docs/` folder
- [ ] Copy your `Data Acquisition.pptx` to `docs/` folder
- [ ] Update README.md with your GitHub username in clone URL
- [ ] Review and customize LICENSE if needed
- [ ] Add any additional team members to contributors list

### For GitHub Upload:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Crime data analysis project"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/crime-data-analysis-ontario.git

# Push to GitHub
git push -u origin main
```

---

## 📊 What Each Analysis Module Does

### 1. Data Cleaning (`src/data_cleaning.py`)
```python
from src.data_cleaning import clean_data

# Clean your data in one line
df = clean_data('Crime Dataset for Data Acquisition.csv')
```

### 2. Visualization (`src/visualization.py`)
```python
from src.visualization import plot_crime_by_city, plot_crime_heatmap

# Create visualizations
plot_crime_by_city(df)
plot_crime_heatmap(df)
```

### 3. Clustering (`src/clustering.py`)
```python
from src.clustering import perform_clustering, plot_clusters

# Perform K-means clustering
labels, X_pca, kmeans, scaler = perform_clustering(df, n_clusters=3)
plot_clusters(X_pca, labels, city_names)
```

### 4. Statistical Tests (`src/statistical_tests.py`)
```python
from src.statistical_tests import perform_ttest, print_ttest_results

# Compare Toronto vs Windsor
results = perform_ttest(df, 'Toronto', 'Windsor')
print_ttest_results(results)
```

### 5. Forecasting (`src/forecasting.py`)
```python
from src.forecasting import prepare_time_series, fit_exponential_smoothing, forecast_crimes

# Forecast 2025 crime levels
ts = prepare_time_series(df)
model = fit_exponential_smoothing(ts)
forecast = forecast_crimes(model, steps=1)
```

---

## 🎯 Key Project Results

### Clustering Results
- **Cluster 1 (High-Risk):** Toronto
- **Cluster 0 (Moderate-Risk):** London, Kitchener-Waterloo
- **Cluster 2 (Low-Risk):** Guelph, Windsor

### Model Performance
| Model | R² | RMSE |
|-------|-----|------|
| Linear Regression | -96.01 | 14,951 |
| Random Forest | 0.944 | 360.43 |

### 2025 Forecast
- **Predicted Total Crimes:** ~504,272 incidents

---

## 📝 Customization Guide

### Adding Your Information

1. **Update README.md:**
   - Replace `yourusername` in clone URLs
   - Add your email/contact
   - Update any project-specific details

2. **Update LICENSE:**
   - Add all team member names
   - Update year if needed

3. **Update CONTRIBUTORS:**
   - Add GitHub usernames
   - Update roles if needed

### Adding New Analysis

1. Create new file in `src/` folder
2. Add import to `src/__init__.py`
3. Document functions with docstrings
4. Update README.md with new features

### Adding New Visualizations

1. Add function to `src/visualization.py`
2. Save outputs to `outputs/figures/`
3. Reference in README.md

---

## 🔗 External Resources

- [Statistics Canada Data](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)

---

## ❓ FAQ

**Q: Do I need to use all the source code files?**  
A: No, they're optional. The main analysis is in your Jupyter notebook.

**Q: Can I modify the documentation?**  
A: Yes! Customize everything to match your project needs.

**Q: What if my dataset is too large for GitHub?**  
A: Use Git LFS or host data externally and link to it.

**Q: How do I add my team members?**  
A: Update the Contributors table in README.md and LICENSE file.

---

## 📞 Support

For questions or issues:
1. Check the [SETUP.md](SETUP.md) troubleshooting section
2. Review [CONTRIBUTING.md](CONTRIBUTING.md)
3. Create an issue on GitHub

---

**Good luck with your project! 🎉**
