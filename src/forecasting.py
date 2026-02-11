"""
Forecasting Module

This module contains functions for time series forecasting
of crime data using exponential smoothing.
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt


def prepare_time_series(df):
    """
    Prepare time series data from dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
        
    Returns:
    --------
    pd.Series
        Time series with year as index
    """
    annual_totals = df.groupby('Year')['Value'].sum()
    return annual_totals


def fit_exponential_smoothing(ts, trend='add', damped_trend=True):
    """
    Fit exponential smoothing model to time series.
    
    Parameters:
    -----------
    ts : pd.Series
        Time series data
    trend : str
        Type of trend ('add', 'mul', or None)
    damped_trend : bool
        Whether to use damped trend
        
    Returns:
    --------
    ExponentialSmoothingResults
        Fitted model results
    """
    model = ExponentialSmoothing(
        ts,
        trend=trend,
        seasonal=None,
        damped_trend=damped_trend
    )
    
    results = model.fit()
    return results


def forecast_crimes(model_results, steps=1):
    """
    Generate forecasts using fitted model.
    
    Parameters:
    -----------
    model_results : ExponentialSmoothingResults
        Fitted exponential smoothing model
    steps : int
        Number of steps to forecast
        
    Returns:
    --------
    pd.Series
        Forecasted values
    """
    forecast = model_results.forecast(steps=steps)
    return forecast


def plot_forecast(ts, forecast, model_results=None, save_path=None):
    """
    Plot time series with forecast.
    
    Parameters:
    -----------
    ts : pd.Series
        Historical time series
    forecast : pd.Series
        Forecasted values
    model_results : ExponentialSmoothingResults, optional
        Fitted model for plotting fitted values
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(12, 6))
    
    # Plot historical data
    plt.plot(ts.index, ts.values, marker='o', linewidth=2, 
             markersize=8, label='Historical', color='blue')
    
    # Plot fitted values if available
    if model_results is not None:
        fitted = model_results.fittedvalues
        plt.plot(fitted.index, fitted.values, '--', 
                label='Fitted', color='green', alpha=0.7)
    
    # Plot forecast
    plt.plot(forecast.index, forecast.values, marker='s', 
             linewidth=2, markersize=8, label='Forecast', color='red')
    
    # Add confidence interval (approximate)
    if model_results is not None:
        resid_std = np.std(model_results.resid)
        upper = forecast + 1.96 * resid_std
        lower = forecast - 1.96 * resid_std
        plt.fill_between(forecast.index, lower, upper, 
                        alpha=0.2, color='red', label='95% CI')
    
    plt.title('Crime Trend and Forecast', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Crime Count', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def calculate_growth_rate(ts):
    """
    Calculate year-over-year growth rates.
    
    Parameters:
    -----------
    ts : pd.Series
        Time series data
        
    Returns:
    --------
    pd.Series
        Growth rates as percentages
    """
    growth_rates = ts.pct_change() * 100
    return growth_rates


def get_model_summary(model_results):
    """
    Get summary statistics from fitted model.
    
    Parameters:
    -----------
    model_results : ExponentialSmoothingResults
        Fitted exponential smoothing model
        
    Returns:
    --------
    dict
        Dictionary with model summary statistics
    """
    summary = {
        'aic': model_results.aic,
        'bic': model_results.bic,
        'mse': np.mean(model_results.resid**2),
        'rmse': np.sqrt(np.mean(model_results.resid**2)),
        'mae': np.mean(np.abs(model_results.resid)),
        'params': model_results.params
    }
    return summary


def simulate_growth_forecast(ts, growth_rate=0.10, years=1):
    """
    Generate forecast based on assumed growth rate.
    
    Parameters:
    -----------
    ts : pd.Series
        Historical time series
    growth_rate : float
        Assumed annual growth rate (decimal)
    years : int
        Number of years to forecast
        
    Returns:
    --------
    pd.Series
        Simulated forecast
    """
    last_value = ts.iloc[-1]
    last_year = ts.index[-1]
    
    forecast_values = []
    forecast_years = []
    
    for i in range(1, years + 1):
        forecast_value = last_value * ((1 + growth_rate) ** i)
        forecast_values.append(forecast_value)
        forecast_years.append(last_year + i)
    
    forecast = pd.Series(forecast_values, index=forecast_years)
    return forecast


if __name__ == '__main__':
    # Example usage
    import data_cleaning as dc
    
    df = dc.clean_data('../Crime Dataset for Data Acquisition.csv')
    
    # Prepare time series
    ts = prepare_time_series(df)
    print("Historical Crime Totals:")
    print(ts)
    
    # Calculate growth rates
    growth_rates = calculate_growth_rate(ts)
    print("\nYear-over-Year Growth Rates (%):")
    print(growth_rates.dropna())
    
    # Fit exponential smoothing model
    model_results = fit_exponential_smoothing(ts)
    
    # Get model summary
    summary = get_model_summary(model_results)
    print("\nModel Summary:")
    print(f"  AIC: {summary['aic']:.2f}")
    print(f"  BIC: {summary['bic']:.2f}")
    print(f"  RMSE: {summary['rmse']:.2f}")
    print(f"  MAE: {summary['mae']:.2f}")
    
    # Generate forecast for 2025
    forecast = forecast_crimes(model_results, steps=1)
    print(f"\nForecast for 2025: {forecast.iloc[0]:,.0f} crimes")
    
    # Plot results
    plot_forecast(ts, forecast, model_results)
    
    # Compare with growth simulation
    sim_forecast = simulate_growth_forecast(ts, growth_rate=0.10, years=1)
    print(f"\nSimulated Forecast (10% growth): {sim_forecast.iloc[0]:,.0f} crimes")
