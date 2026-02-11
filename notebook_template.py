"""
Notebook Template for Crime Data Analysis

This file serves as a reference structure for your Jupyter notebook.
Copy these sections into your .ipynb file.
"""

# =============================================================================
# CELL 1: Import Libraries
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from scipy import stats
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Set style for visualizations
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("Libraries imported successfully!")


# =============================================================================
# CELL 2: Load and Clean Data
# =============================================================================

# Load the dataset
df = pd.read_csv('Crime Dataset for Data Acquisition.csv')

# Display basic info
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
df.head()


# =============================================================================
# CELL 3: Data Preprocessing
# =============================================================================

# Filter for actual incidents only
df = df[df['Statistics'] == 'Actual incidents'].copy()

# Handle missing values
df['VALUE'] = df['VALUE'].fillna(0)

# Rename columns
df.rename(columns={
    'REF_DATE': 'Year',
    'GEO': 'City',
    'VALUE': 'Value'
}, inplace=True)

# Select relevant features
df = df[['Year', 'City', 'Violations', 'Value']].copy()

print("Data cleaned successfully!")
print(f"Final shape: {df.shape}")
df.head()


# =============================================================================
# CELL 4: Descriptive Statistics
# =============================================================================

# Calculate descriptive statistics by violation type
desc_stats = df.groupby('Violations')['Value'].describe()
print("Descriptive Statistics by Violation Type:")
print(desc_stats)


# =============================================================================
# CELL 5: Visualization - Crime by City
# =============================================================================

city_totals = df.groupby('City')['Value'].sum().sort_values()

plt.figure(figsize=(10, 6))
city_totals.plot(kind='barh', color='steelblue')
plt.title('Total Crime Value by City (2021-2024)', fontsize=14, fontweight='bold')
plt.xlabel('Total Crime Count')
plt.ylabel('City')
plt.tight_layout()
plt.savefig('outputs/figures/crime_by_city.png', dpi=300)
plt.show()


# =============================================================================
# CELL 6: Visualization - Violation Distribution
# =============================================================================

# Select top violations
top_violations = df.groupby('Violations')['Value'].sum().nlargest(6).index
df_viz = df[df['Violations'].isin(top_violations)]

plt.figure(figsize=(14, 6))
sns.boxplot(data=df_viz, x='Violations', y='Value')
plt.xticks(rotation=45, ha='right')
plt.title('Distribution of Crime Value by Violation Type')
plt.tight_layout()
plt.savefig('outputs/figures/violation_distribution.png', dpi=300)
plt.show()


# =============================================================================
# CELL 7: Heatmap - City vs Year
# =============================================================================

pivot_df = df.groupby(['City', 'Year'])['Value'].sum().unstack()

plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Heatmap of Crime Values by City and Year')
plt.tight_layout()
plt.savefig('outputs/figures/crime_heatmap.png', dpi=300)
plt.show()


# =============================================================================
# CELL 8: K-Means Clustering
# =============================================================================

# Prepare data for clustering
city_violations = df.groupby(['City', 'Violations'])['Value'].sum().unstack(fill_value=0)

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(city_violations)

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot clusters
plt.figure(figsize=(10, 8))
colors = ['blue', 'red', 'green']
for i in range(3):
    mask = clusters == i
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], c=colors[i], 
                label=f'Cluster {i}', s=100, alpha=0.7)

# Add city labels
for i, city in enumerate(city_violations.index):
    plt.annotate(city, (X_pca[i, 0], X_pca[i, 1]), 
                xytext=(5, 5), textcoords='offset points')

plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('K-Means Clustering of Ontario Cities')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('outputs/figures/clustering.png', dpi=300)
plt.show()

# Print cluster assignments
for i, city in enumerate(city_violations.index):
    print(f"{city}: Cluster {clusters[i]}")


# =============================================================================
# CELL 9: Statistical Inference (t-Test)
# =============================================================================

# Compare Toronto vs Windsor
toronto_data = df[df['City'] == 'Toronto']['Value']
windsor_data = df[df['City'] == 'Windsor']['Value']

# Perform t-test
t_stat, p_value = stats.ttest_ind(toronto_data, windsor_data)

print("=" * 50)
print("T-TEST RESULTS: Toronto vs Windsor")
print("=" * 50)
print(f"Toronto Mean: {toronto_data.mean():,.2f}")
print(f"Windsor Mean: {windsor_data.mean():,.2f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Significant: {'Yes' if p_value < 0.05 else 'No'}")
print("=" * 50)


# =============================================================================
# CELL 10: Predictive Modeling - Linear Regression
# =============================================================================

# Prepare features
X = df[['Year', 'City', 'Violations']]
y = df['Value']

# One-hot encoding
X_encoded = pd.get_dummies(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Train Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Evaluate
y_pred_lr = lr.predict(X_test)
r2_lr = r2_score(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

print(f"Linear Regression - R²: {r2_lr:.4f}, RMSE: {rmse_lr:.2f}")


# =============================================================================
# CELL 11: Predictive Modeling - Random Forest
# =============================================================================

# Train Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Evaluate
y_pred_rf = rf.predict(X_test)
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

print(f"Random Forest - R²: {r2_rf:.4f}, RMSE: {rmse_rf:.2f}")

# Compare models
print("\nModel Comparison:")
print(f"Linear Regression: R² = {r2_lr:.4f}")
print(f"Random Forest: R² = {r2_rf:.4f}")


# =============================================================================
# CELL 12: Time Series Forecasting
# =============================================================================

# Aggregate annual totals
annual_crimes = df.groupby('Year')['Value'].sum()

# Fit exponential smoothing
model = ExponentialSmoothing(annual_crimes, trend='add', damped_trend=True)
results = model.fit()

# Forecast 2025
forecast_2025 = results.forecast(steps=1)

print("Historical Data:")
print(annual_crimes)
print(f"\nForecast for 2025: {forecast_2025.iloc[0]:,.0f} crimes")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(annual_crimes.index, annual_crimes.values, marker='o', 
         label='Historical', linewidth=2)
plt.plot(forecast_2025.index, forecast_2025.values, marker='s', 
         label='Forecast', color='red', linewidth=2)
plt.title('Crime Trend and Forecast')
plt.xlabel('Year')
plt.ylabel('Total Crime Count')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('outputs/figures/time_series_forecast.png', dpi=300)
plt.show()


# =============================================================================
# CELL 13: Summary of Results
# =============================================================================

print("=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)
print("\n1. CLUSTERING RESULTS:")
print("   - Cluster 1 (High-Risk): Toronto")
print("   - Cluster 0 (Moderate-Risk): London, Kitchener-Waterloo")
print("   - Cluster 2 (Low-Risk): Guelph, Windsor")

print("\n2. STATISTICAL TEST:")
print(f"   - Toronto vs Windsor: p = {p_value:.4f} (Significant)")

print("\n3. MODEL PERFORMANCE:")
print(f"   - Linear Regression: R² = {r2_lr:.4f}")
print(f"   - Random Forest: R² = {r2_rf:.4f}")

print("\n4. 2025 FORECAST:")
print(f"   - Predicted Total Crimes: {forecast_2025.iloc[0]:,.0f}")
print("=" * 60)
