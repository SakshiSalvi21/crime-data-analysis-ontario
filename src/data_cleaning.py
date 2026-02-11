"""
Data Cleaning Module

This module contains functions for cleaning and preprocessing
the crime dataset.
"""

import pandas as pd
import numpy as np


def load_data(filepath):
    """
    Load crime data from CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    df = pd.read_csv(filepath)
    return df


def filter_actual_incidents(df):
    """
    Filter dataset to include only actual incidents.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw dataframe
        
    Returns:
    --------
    pd.DataFrame
        Filtered dataframe
    """
    return df[df['Statistics'] == 'Actual incidents'].copy()


def handle_missing_values(df, strategy='zero'):
    """
    Handle missing values in the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    strategy : str
        Strategy for handling missing values ('zero', 'mean', 'drop')
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with handled missing values
    """
    if strategy == 'zero':
        df['VALUE'] = df['VALUE'].fillna(0)
    elif strategy == 'mean':
        df['VALUE'] = df['VALUE'].fillna(df['VALUE'].mean())
    elif strategy == 'drop':
        df = df.dropna(subset=['VALUE'])
    return df


def rename_columns(df):
    """
    Rename columns for clarity.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with renamed columns
    """
    column_mapping = {
        'REF_DATE': 'Year',
        'GEO': 'City',
        'VALUE': 'Value'
    }
    return df.rename(columns=column_mapping)


def select_features(df):
    """
    Select relevant features for analysis.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with selected features
    """
    features = ['Year', 'City', 'Violations', 'Value']
    return df[features].copy()


def clean_data(filepath, missing_strategy='zero'):
    """
    Complete data cleaning pipeline.
    
    Parameters:
    -----------
    filepath : str
        Path to the raw data file
    missing_strategy : str
        Strategy for handling missing values
        
    Returns:
    --------
    pd.DataFrame
        Cleaned dataframe ready for analysis
    """
    # Load data
    df = load_data(filepath)
    
    # Filter for actual incidents
    df = filter_actual_incidents(df)
    
    # Handle missing values
    df = handle_missing_values(df, strategy=missing_strategy)
    
    # Rename columns
    df = rename_columns(df)
    
    # Select features
    df = select_features(df)
    
    return df


if __name__ == '__main__':
    # Example usage
    df_clean = clean_data('../Crime Dataset for Data Acquisition.csv')
    print(f"Cleaned dataset shape: {df_clean.shape}")
    print(df_clean.head())
