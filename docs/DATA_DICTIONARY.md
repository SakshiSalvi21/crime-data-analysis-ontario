# Data Dictionary

## Crime Dataset for Data Acquisition

---

## Overview

This document provides detailed information about the dataset used in the Crime Data Analysis of Ontario Cities project.

**Dataset Name:** Crime Dataset for Data Acquisition.csv  
**Source:** Statistics Canada  
**Time Period:** 2021-2024  
**Geographic Coverage:** 5 Ontario cities  
**Total Records:** Varies by city and violation type

---

## Variables

### 1. REF_DATE

| Attribute | Value |
|-----------|-------|
| **Name** | REF_DATE |
| **Renamed To** | Year |
| **Type** | Integer |
| **Description** | Year of incident reporting |
| **Range** | 2021 - 2024 |
| **Example** | 2021, 2022, 2023, 2024 |
| **Usage** | Time series analysis, trend identification |

### 2. GEO

| Attribute | Value |
|-----------|-------|
| **Name** | GEO |
| **Renamed To** | City |
| **Type** | Categorical (String) |
| **Description** | Geographic location/municipality |
| **Categories** | Toronto, Windsor, Guelph, London, Kitchener-Waterloo-Cambridge |
| **Example** | "Toronto" |
| **Usage** | City-wise comparisons, clustering |

### 3. Violations

| Attribute | Value |
|-----------|-------|
| **Name** | Violations |
| **Type** | Categorical (String) |
| **Description** | Type of criminal violation |
| **Categories** | See Violation Types below |
| **Example** | "Assault, level 1" |
| **Usage** | Crime type analysis, pattern identification |

### 4. Statistics

| Attribute | Value |
|-----------|-------|
| **Name** | Statistics |
| **Type** | Categorical (String) |
| **Description** | Type of statistical measure |
| **Categories** | Actual incidents, Rate per 100,000, Cleared, Unfounded |
| **Filter Used** | "Actual incidents" only |
| **Usage** | Data filtering and consistency |

### 5. VALUE

| Attribute | Value |
|-----------|-------|
| **Name** | VALUE |
| **Renamed To** | Value |
| **Type** | Numeric (Integer) |
| **Description** | Crime count or rate value |
| **Range** | 0 - 304,082 |
| **Unit** | Number of incidents |
| **Example** | 25,184 |
| **Usage** | Primary analysis variable |

---

## Violation Types

### High-Frequency Violations

| Violation Type | Description | Avg Count |
|----------------|-------------|-----------|
| Total, all Criminal Code violations | Aggregate of all Criminal Code offenses | 72,119 |
| Assault, level 1 | Minor physical assault | 6,137 |
| Sexual assault | Sexual offenses | 1,089 |
| Robbery | Theft with force or threat | 1,023 |
| Impaired driving | Driving under influence | ~1,000 |
| Drug violations | Drug-related offenses | ~1,000 |

### Low-Frequency Violations

| Violation Type | Description | Avg Count |
|----------------|-------------|-----------|
| Homicide | Murder and manslaughter | 12 |
| Attempted murder | Failed homicide attempts | <10 |
| Criminal negligence causing death | Death by negligence | <5 |

---

## City Profiles

### Toronto
- **Population:** ~2.9 million
- **Crime Level:** High
- **Total Incidents (2021-2024):** > 2.4 million
- **Characteristics:** Metropolitan, highest volume

### London
- **Population:** ~400,000
- **Crime Level:** Moderate
- **Total Incidents (2021-2024):** Mid-range
- **Characteristics:** Mid-sized city

### Kitchener-Waterloo-Cambridge
- **Population:** ~500,000
- **Crime Level:** Moderate
- **Total Incidents (2021-2024):** Mid-range
- **Characteristics:** Tri-city area

### Windsor
- **Population:** ~230,000
- **Crime Level:** Low
- **Total Incidents (2021-2024):** Low
- **Characteristics:** Border city

### Guelph
- **Population:** ~130,000
- **Crime Level:** Low
- **Total Incidents (2021-2024):** Lowest
- **Characteristics:** University town

---

## Data Quality

### Completeness
- Missing values: < 1% in VALUE column
- Missing handling: Imputed with 0 or removed

### Consistency
- All years have complete data for all cities
- Violation types consistent across cities

### Accuracy
- Source: Official Statistics Canada data
- Verified against published reports

---

## Derived Variables

### Created During Analysis

| Variable | Description | Calculation |
|----------|-------------|-------------|
| Year | Renamed from REF_DATE | Direct mapping |
| City | Renamed from GEO | Direct mapping |
| Crime_Rate | Rate per 100,000 | (Value / Population) × 100,000 |
| Log_Value | Log-transformed count | log(Value + 1) |

---

## Data Relationships

### Hierarchical Structure
```
Year (2021-2024)
  └── City (5 cities)
        └── Violation Type (multiple)
              └── Statistics type
                    └── Value
```

### Key Relationships
- One city has many violation types
- One year has data for all cities
- Each city-violation-year combination has one value

---

## Usage Notes

### For Analysis
- Use "Actual incidents" for raw counts
- Consider population differences when comparing cities
- Account for year-over-year trends

### For Modeling
- One-hot encode categorical variables
- Scale numeric features for clustering
- Handle outliers appropriately

### For Visualization
- Use log scale for highly skewed distributions
- Consider normalization for comparisons
- Label axes clearly

---

## Data Source Citation

```
Government of Canada, Statistics Canada. (2025, July 22). 
Incident-based crime statistics, by detailed violations, Canada, 
provinces, territories, Census Metropolitan Areas and Canadian 
Forces Military Police. 
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701
```

---

## Updates and Versions

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | July 2025 | Initial dataset |

---

For questions about the data, contact the Statistics Canada help desk or refer to their official documentation.
