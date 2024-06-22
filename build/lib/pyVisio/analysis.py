import numpy as np
import statsmodels.api as sm
import pandas as pd

def time_series_analysis(data, lags=1, detect_anomalies=False):
    model = sm.tsa.ARIMA(data, order=(lags, 1, 0))
    fit = model.fit(disp=0)
    forecast = fit.predict(start=len(data), end=len(data) + 10)
    if detect_anomalies:
        anomalies = detect_anomalies_in_series(data)
        return fit.summary(), forecast, anomalies
    return fit.summary(), forecast

def detect_anomalies_in_series(data):
    # Basit anomali tespiti
    data_mean = np.mean(data)
    data_std = np.std(data)
    anomaly_cutoff = data_std * 2
    lower_limit = data_mean - anomaly_cutoff
    upper_limit = data_mean + anomaly_cutoff
    anomalies = [(i, x) for i, x in enumerate(data) if x < lower_limit or x > upper_limit]
    return anomalies
