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
    model = ARIMA(data, order=(lags, 1, 0))
    fit = model.fit()
    return fit.summary(), fit.predict(start=len(data), end=len(data) + 10)

def detect_anomalies_in_series(data):
    # Basit anomali tespiti
    data_mean = np.mean(data)
    data_std = np.std(data)
    anomaly_cutoff = data_std * 2
    lower_limit = data_mean - anomaly_cutoff
    upper_limit = data_mean + anomaly_cutoff
    anomalies = [(i, x) for i, x in enumerate(data) if x < lower_limit or x > upper_limit]
    return anomalies
