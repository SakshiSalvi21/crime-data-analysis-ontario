# Detailed Methodology

## Crime Data Analysis of Ontario Cities (2021-2024)

---

## Table of Contents

1. [Data Collection](#data-collection)
2. [Data Preprocessing](#data-preprocessing)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
4. [Clustering Analysis](#clustering-analysis)
5. [Statistical Inference](#statistical-inference)
6. [Predictive Modeling](#predictive-modeling)
7. [Time Series Forecasting](#time-series-forecasting)

---

## Data Collection

### Source
- **Primary Source:** Statistics Canada
- **Dataset:** Incident-based crime statistics
- **URL:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701
- **Access Date:** July 2025

### Dataset Characteristics
- **Time Period:** 2021-2024
- **Geographic Coverage:** 5 Ontario cities
- **Total Records:** Multiple violation types across 4 years

### Variables Description

| Variable | Type | Description |
|----------|------|-------------|
| REF_DATE | Numeric | Year of incident reporting |
| GEO | Categorical | City/municipality name |
| Violations | Categorical | Type of criminal violation |
| Statistics | Categorical | Statistical measure type |
| VALUE | Numeric | Crime count or rate value |
| DGUID | Identifier | Geographic identifier |
| UOM | Categorical | Unit of measure |

---

## Data Preprocessing

### Step 1: Filtering
```python
# Filter for actual incidents only
df_filtered = df[df['Statistics'] == 'Actual incidents']
```

**Rationale:** Ensures consistency by using only raw reported crime counts, not rates or cleared cases.

### Step 2: Missing Value Treatment
- Identified missing values in VALUE column
- Applied context-based imputation (0 for missing counts)
- Removed rows with critical missing information

### Step 3: Feature Engineering
```python
# Column renaming for clarity
df.rename(columns={
    'REF_DATE': 'Year',
    'GEO': 'City',
    'VALUE': 'Value'
}, inplace=True)
```

### Step 4: Feature Selection
**Retained:**
- Year
- City
- Violations
- Value

**Dropped:**
- DGUID (identifier, not meaningful for analysis)
- UOM_ID (redundant)
- VECTOR (metadata)
- Coordinate columns

### Step 5: Encoding
```python
# One-hot encoding for categorical variables
df_encoded = pd.get_dummies(df, columns=['City', 'Violations'])
```

---

## Exploratory Data Analysis

### Descriptive Statistics

Calculated for each violation type:
- Count
- Mean
- Standard Deviation
- Minimum/Maximum
- Quartiles (25%, 50%, 75%)

### Key Findings from EDA

| Violation Type | Mean | Std Dev | Max |
|----------------|------|---------|-----|
| Total Criminal Code | 72,119 | 68,432 | 304,082 |
| Assault, Level 1 | 6,137 | 8,898 | 26,821 |
| Sexual Assault | 1,089 | 1,523 | 4,987 |
| Robbery | 1,023 | 1,456 | 5,234 |
| Homicide | 12 | 28 | 89 |

### Visualization Techniques

1. **Horizontal Bar Chart**
   - Shows total crime by city
   - Highlights Toronto's dominance

2. **Boxplot**
   - Displays distribution by violation type
   - Identifies outliers

3. **Heatmap**
   - City vs Year matrix
   - Color-coded crime values

---

## Clustering Analysis

### Algorithm: K-Means Clustering

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

### Optimal Clusters

Determined using:
- Elbow method
- Silhouette score
- Domain knowledge

**Final Selection:** 3 clusters

### Cluster Profiles

| Cluster | Cities | Profile |
|---------|--------|---------|
| 0 | London, Kitchener-Waterloo | Moderate crime levels |
| 1 | Toronto | High crime volume |
| 2 | Guelph, Windsor | Low crime levels |

### PCA Results
- Component 1 explains ~65% variance
- Component 2 explains ~20% variance
- Clear separation between clusters in 2D space

---

## Statistical Inference

### Hypothesis Test: Toronto vs Windsor

**Null Hypothesis (H₀):** μ_Toronto = μ_Windsor  
**Alternative Hypothesis (H₁):** μ_Toronto ≠ μ_Windsor

### Test Selection
- **Test Type:** Independent Samples t-Test
- **Assumptions:**
  - Independent samples
  - Approximately normal distribution
  - Equal variances (tested with Levene's test)

### Implementation
```python
from scipy import stats

# Extract data for each city
toronto_crimes = df[df['City'] == 'Toronto']['Value']
windsor_crimes = df[df['City'] == 'Windsor']['Value']

# Perform t-test
t_stat, p_value = stats.ttest_ind(toronto_crimes, windsor_crimes)
```

### Results

| Metric | Value |
|--------|-------|
| t-statistic | 2.1115 |
| p-value | 0.0329 |
| Significance Level | 0.05 |
| Degrees of Freedom | 38 |

**Conclusion:** Reject H₀ (p < 0.05). Significant difference exists.

---

## Predictive Modeling

### Model 1: Linear Regression

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Prepare data
X = df[['Year', 'City', 'Violations']]
y = df['Value']

# One-hot encoding
X_encoded = pd.get_dummies(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Train model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Evaluate
y_pred = lr.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
```

**Results:**
- R² = -96.01
- RMSE = 14,951
- Status: ❌ Poor performance

### Model 2: Random Forest Regression

```python
from sklearn.ensemble import RandomForestRegressor

# Train model
rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
rf.fit(X_train, y_train)

# Evaluate
y_pred_rf = rf.predict(X_test)
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
```

**Results:**
- R² = 0.944
- RMSE = 360.43
- Status: ✅ Excellent performance

### Feature Importance

| Feature | Importance |
|---------|------------|
| City_Toronto | 0.35 |
| Violation_Total | 0.28 |
| Year | 0.15 |
| Violation_Assault | 0.12 |
| Other features | 0.10 |

### Model Comparison

| Metric | Linear Regression | Random Forest |
|--------|------------------|---------------|
| R² | -96.01 | 0.944 |
| RMSE | 14,951 | 360.43 |
| Prediction (Toronto 2024) | 33,093 | 25,184 |

---

## Time Series Forecasting

### Method: Exponential Smoothing

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Aggregate annual totals
annual_crimes = df.groupby('Year')['Value'].sum()

# Fit model
model = ExponentialSmoothing(
    annual_crimes,
    trend='add',
    seasonal=None,
    damped_trend=True
)
results = model.fit()

# Forecast 2025
forecast_2025 = results.forecast(steps=1)
```

### Model Parameters

| Parameter | Value |
|-----------|-------|
| Trend | Additive |
| Seasonality | None (annual data) |
| Damping | Enabled |
| Smoothing Level (α) | 0.3 |
| Smoothing Trend (β) | 0.1 |

### Historical Data

| Year | Total Crimes |
|------|--------------|
| 2021 | 362,000 |
| 2022 | 398,000 |
| 2023 | 445,000 |
| 2024 | 458,000 |

### Forecast Result

| Year | Forecast | Confidence Interval |
|------|----------|---------------------|
| 2025 | 504,272 | ±25,000 |

### Growth Rate Analysis

```
Year-over-year growth:
2021-2022: +10.0%
2022-2023: +11.8%
2023-2024: +2.9%
Average: +8.2%
```

---

## Validation and Limitations

### Model Validation
- Cross-validation (k=5)
- Train-test split (80-20)
- Residual analysis

### Limitations
1. Limited time series data (4 years)
2. No demographic or socioeconomic variables
3. Reporting bias may affect actual incident counts
4. Seasonal patterns not captured in annual aggregation

### Future Improvements
1. Include more years of data
2. Add demographic features
3. Implement seasonal decomposition
4. Try advanced models (LSTM, Prophet)
5. Include more Ontario cities

---

## References

1. Statistics Canada. (2025). Incident-based crime statistics.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An Introduction to Statistical Learning.
3. Hyndman, R.J., & Athanasopoulos, G. (2018). Forecasting: Principles and Practice.
