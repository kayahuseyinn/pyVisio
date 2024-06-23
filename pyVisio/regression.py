import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

def linear_regression(x, y):
    x = sm.add_constant(x)  # Add constant term for intercept
    model = sm.OLS(y, x).fit()
    predictions = model.predict(x)
    return model.summary(), predictions

def time_series_analysis(data, lags=1):
    """
    Perform time series analysis.

    Parameters:
        data (array-like): The time series data.
        lags (int, optional): The number of lags to use. Default is 1.

    Returns:
        summary: Summary of the ARIMA model.
        forecast: Forecasted values.
        anomalies: Detected anomalies (if any).
    """
    model = sm.tsa.ARIMA(data, order=(lags, 1, 0))
    fit = model.fit()
    forecast = fit.forecast(steps=10)
    
    # Dummy anomaly detection for demonstration purposes
    anomalies = np.where(np.abs(data - fit.fittedvalues) > 2 * np.std(data), True, False)
    
    return fit.summary(), forecast, anomalies

def detect_anomalies_in_series(data):
    # Basit anomali tespiti
    data_mean = np.mean(data)
    data_std = np.std(data)
    anomaly_cutoff = data_std * 2
    lower_limit = data_mean - anomaly_cutoff
    upper_limit = data_mean + anomaly_cutoff
    anomalies = [(i, x) for i, x in enumerate(data) if x < lower_limit or x > upper_limit]
    return anomalies
