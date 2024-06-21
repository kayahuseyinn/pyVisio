import numpy as np
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
