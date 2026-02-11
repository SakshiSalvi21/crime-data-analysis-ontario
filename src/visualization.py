"""
Visualization Module

This module contains functions for creating visualizations
for the crime data analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def set_style():
    """Set default plotting style."""
    sns.set_style('whitegrid')
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10


def plot_crime_by_city(df, save_path=None):
    """
    Create horizontal bar chart of total crime by city.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    save_path : str, optional
        Path to save the figure
    """
    set_style()
    
    city_totals = df.groupby('City')['Value'].sum().sort_values()
    
    plt.figure(figsize=(10, 6))
    city_totals.plot(kind='barh', color='steelblue')
    plt.title('Total Crime Value by City (2021-2024)', fontsize=14, fontweight='bold')
    plt.xlabel('Total Crime Count', fontsize=12)
    plt.ylabel('City', fontsize=12)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_violation_distribution(df, save_path=None):
    """
    Create boxplot of crime distribution by violation type.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    save_path : str, optional
        Path to save the figure
    """
    set_style()
    
    # Select top violations for clarity
    top_violations = df.groupby('Violations')['Value'].sum().nlargest(8).index
    df_filtered = df[df['Violations'].isin(top_violations)]
    
    plt.figure(figsize=(14, 6))
    sns.boxplot(data=df_filtered, x='Violations', y='Value')
    plt.xticks(rotation=45, ha='right')
    plt.title('Distribution of Crime Value by Violation Type', fontsize=14, fontweight='bold')
    plt.xlabel('Violation Type', fontsize=12)
    plt.ylabel('Crime Count', fontsize=12)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_crime_heatmap(df, save_path=None):
    """
    Create heatmap of crime values by city and year.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    save_path : str, optional
        Path to save the figure
    """
    set_style()
    
    pivot_df = df.groupby(['City', 'Year'])['Value'].sum().unstack()
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_df, annot=True, fmt='.0f', cmap='YlOrRd', cbar_kws={'label': 'Crime Count'})
    plt.title('Heatmap of Crime Values by City and Year', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('City', fontsize=12)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_time_series(df, save_path=None):
    """
    Create time series plot of annual crime totals.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
    save_path : str, optional
        Path to save the figure
    """
    set_style()
    
    annual_totals = df.groupby('Year')['Value'].sum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(annual_totals.index, annual_totals.values, marker='o', linewidth=2, markersize=8)
    plt.title('Total Crime Trend (2021-2024)', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Crime Count', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    # Example usage
    import data_cleaning as dc
    
    df = dc.clean_data('../Crime Dataset for Data Acquisition.csv')
    
    plot_crime_by_city(df)
    plot_violation_distribution(df)
    plot_crime_heatmap(df)
    plot_time_series(df)
