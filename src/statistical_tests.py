"""
Statistical Tests Module

This module contains functions for performing statistical inference
tests on the crime data.
"""

import pandas as pd
import numpy as np
from scipy import stats


def perform_ttest(df, city1, city2):
    """
    Perform independent samples t-test between two cities.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    city1 : str
        Name of first city
    city2 : str
        Name of second city
        
    Returns:
    --------
    dict
        Dictionary with test results
    """
    # Extract data for each city
    city1_data = df[df['City'] == city1]['Value']
    city2_data = df[df['City'] == city2]['Value']
    
    # Perform independent t-test
    t_stat, p_value = stats.ttest_ind(city1_data, city2_data)
    
    # Calculate means
    mean1 = city1_data.mean()
    mean2 = city2_data.mean()
    
    # Calculate standard deviations
    std1 = city1_data.std()
    std2 = city2_data.std()
    
    # Determine significance
    alpha = 0.05
    is_significant = p_value < alpha
    
    results = {
        'city1': city1,
        'city2': city2,
        'city1_mean': mean1,
        'city2_mean': mean2,
        'city1_std': std1,
        'city2_std': std2,
        'city1_n': len(city1_data),
        'city2_n': len(city2_data),
        't_statistic': t_stat,
        'p_value': p_value,
        'alpha': alpha,
        'is_significant': is_significant,
        'degrees_of_freedom': len(city1_data) + len(city2_data) - 2
    }
    
    return results


def print_ttest_results(results):
    """
    Print formatted t-test results.
    
    Parameters:
    -----------
    results : dict
        Results dictionary from perform_ttest
    """
    print("=" * 60)
    print("INDEPENDENT SAMPLES T-TEST RESULTS")
    print("=" * 60)
    print(f"\nHypothesis:")
    print(f"  H₀: μ_{results['city1']} = μ_{results['city2']}")
    print(f"  H₁: μ_{results['city1']} ≠ μ_{results['city2']}")
    
    print(f"\nDescriptive Statistics:")
    print(f"  {results['city1']}:")
    print(f"    Mean: {results['city1_mean']:,.2f}")
    print(f"    Std Dev: {results['city1_std']:,.2f}")
    print(f"    N: {results['city1_n']}")
    print(f"  {results['city2']}:")
    print(f"    Mean: {results['city2_mean']:,.2f}")
    print(f"    Std Dev: {results['city2_std']:,.2f}")
    print(f"    N: {results['city2_n']}")
    
    print(f"\nTest Results:")
    print(f"  t-statistic: {results['t_statistic']:.4f}")
    print(f"  p-value: {results['p_value']:.4f}")
    print(f"  Degrees of Freedom: {results['degrees_of_freedom']}")
    print(f"  Significance Level (α): {results['alpha']}")
    
    print(f"\nConclusion:")
    if results['is_significant']:
        print(f"  ✓ REJECT the null hypothesis (p < α)")
        print(f"  ✓ Significant difference exists between {results['city1']} and {results['city2']}")
    else:
        print(f"  ✗ FAIL TO REJECT the null hypothesis (p ≥ α)")
        print(f"  ✗ No significant difference between {results['city1']} and {results['city2']}")
    print("=" * 60)


def perform_anova(df, cities):
    """
    Perform one-way ANOVA across multiple cities.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    cities : list
        List of city names to compare
        
    Returns:
    --------
    dict
        Dictionary with ANOVA results
    """
    # Extract data for each city
    city_data = [df[df['City'] == city]['Value'] for city in cities]
    
    # Perform one-way ANOVA
    f_stat, p_value = stats.f_oneway(*city_data)
    
    results = {
        'cities': cities,
        'f_statistic': f_stat,
        'p_value': p_value,
        'alpha': 0.05,
        'is_significant': p_value < 0.05
    }
    
    return results


def levene_test(df, city1, city2):
    """
    Perform Levene's test for equality of variances.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    city1 : str
        Name of first city
    city2 : str
        Name of second city
        
    Returns:
    --------
    dict
        Dictionary with test results
    """
    city1_data = df[df['City'] == city1]['Value']
    city2_data = df[df['City'] == city2]['Value']
    
    stat, p_value = stats.levene(city1_data, city2_data)
    
    return {
        'statistic': stat,
        'p_value': p_value,
        'equal_variances': p_value > 0.05
    }


if __name__ == '__main__':
    # Example usage
    import data_cleaning as dc
    
    df = dc.clean_data('../Crime Dataset for Data Acquisition.csv')
    
    # Perform t-test between Toronto and Windsor
    results = perform_ttest(df, 'Toronto', 'Windsor')
    print_ttest_results(results)
