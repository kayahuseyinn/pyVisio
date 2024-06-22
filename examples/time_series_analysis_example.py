import pyVisio as pv
import numpy as np

data_ts = np.random.randn(100)
summary, forecast, anomalies = pv.time_series_analysis(data_ts, detect_anomalies=True)
print(summary)
print("Forecast:", forecast)
print("Anomalies:", anomalies)
