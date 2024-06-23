import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

def time_series_analysis(data, lags=1, detect_anomalies=False, anomaly_threshold=3):
    model = ARIMA(data, order=(lags, 1, 0))
    fit = model.fit()
    forecast = fit.forecast(steps=10)
    summary = fit.summary()
    
    anomalies = None
    if detect_anomalies:
        anomalies = detect_anomalies_in_series(data, threshold=anomaly_threshold)
    
    return summary, forecast, anomalies

def detect_anomalies_in_series(data, threshold=3):
    data_mean = np.mean(data)
    data_std = np.std(data)
    anomalies = [x for x in data if abs(x - data_mean) > threshold * data_std]
    return anomalies
