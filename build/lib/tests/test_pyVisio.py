import pyVisio as pv
import numpy as np
import time

# 1. Line Chart
data = [1, 2, 3, 4, 5]
pv.line_chart(data, title="Line Chart", xlabel="X Axis", ylabel="Y Axis", color='red')

# 2. Interactive Line Chart
pv.line_chart(data, title="Interactive Line Chart", xlabel="X Axis", ylabel="Y Axis", interactive=True, color='green')

# 3. Bar Chart
data_bar = {'A': 10, 'B': 20, 'C': 30}
pv.bar_chart(data_bar, title="Bar Chart", xlabel="Category", ylabel="Value", color='blue')

# 4. Interactive Bar Chart
pv.bar_chart(data_bar, title="Interactive Bar Chart", xlabel="Category", ylabel="Value", interactive=True, color='purple')

# 5. Scatter Plot
x_data = [1, 2, 3, 4, 5]
y_data = [10, 14, 12, 15, 10]
pv.scatter_plot(x_data, y_data, title="Scatter Plot", xlabel="X Axis", ylabel="Y Axis", color='blue')

# 6. Interactive Scatter Plot
pv.scatter_plot(x_data, y_data, title="Interactive Scatter Plot", xlabel="X Axis", ylabel="Y Axis", interactive=True, color='orange')

# 7. Pie Chart
data_pie = {'Apple': 50, 'Pear': 30, 'Cherry': 20}
pv.pie_chart(data_pie, title="Pie Chart")

# 8. Interactive Pie Chart
pv.pie_chart(data_pie, title="Interactive Pie Chart", interactive=True)

# 9. Time Series Analysis
data_ts = np.random.randn(100)
summary, forecast, anomalies = pv.time_series_analysis(data_ts, lags=1)
print("Summary:", summary)
print("Forecast:", forecast)
print("Anomalies:", anomalies)

# 10. Anomaly Detection
anomalies = pv.detect_anomalies_in_series(data_ts)
print("Anomalies:", anomalies)

# 11. Data Cleaning
raw_data = {'column1': [1, 2, None, 4, 5], 'column2': [5, None, 3, 2, 1]}
cleaned_data = pv.clean_data(raw_data, method='fillna', fill_value=0)
pv.line_chart(cleaned_data['column1'], title="Line Chart with Cleaned Data")

# 12. Setting Themes
custom_theme = {
    'background_color': 'black',
    'grid_color': 'gray',
    'line_color': 'cyan',
    'font_family': 'Arial'
}
pv.set_theme(custom_theme)
pv.line_chart([1, 2, 3, 4, 5], title="Line Chart with Custom Theme")

# 13. Live Line Chart
def update_line_chart(data):
    ani = pv.live_line_chart(data, title="Live Line Chart", xlabel="X Axis", ylabel="Y Axis", color='red')
    return ani

data = [1, 2, 3, 4, 5]
ani_list = []
for i in range(10):
    data.append(data[-1] + np.random.randn())  # Simulating new data point
    ani = update_line_chart(data)
    ani_list.append(ani)
    time.sleep(1)

# 14. Live Bar Chart
def update_bar_chart(data_bar):
    ani = pv.live_bar_chart(data_bar, title="Live Bar Chart", xlabel="Category", ylabel="Value", color='blue')
    return ani

data_bar = {'A': 10, 'B': 20, 'C': 30}
ani_list = []
for i in range(10):
    data_bar['A'] += 1
    data_bar['B'] += 2
    data_bar['C'] += 3
    ani = update_bar_chart(data_bar)
    ani_list.append(ani)
    time.sleep(1)

# 15. Basic Analysis
data = [1, 2, 3, 4, 5]
analysis = pv.basic_analysis(data)
print("Basic Analysis:", analysis)

# 16. Advanced Analysis
data = [1, 2, 3, 4, 5]
advanced_analysis = pv.advanced_analysis(data)
print("Advanced Analysis:", advanced_analysis)

# 17. Generate Report
report_data = {
    'title': 'Data Analysis Report',
    'author': 'Huseyin Kaya',
    'date': '2024-06-22',
    'content': [
        {'type': 'line_chart', 'data': [1, 2, 3, 4, 5], 'title': 'Line Chart'},
        {'type': 'bar_chart', 'data': {'A': 10, 'B': 20, 'C': 30}, 'title': 'Bar Chart'},
        {'type': 'table', 'data': {'Column 1': [1, 2, 3], 'Column 2': [4, 5, 6]}, 'title': 'Sample Table'}
    ]
}
pv.generate_report(report_data, format='pdf', output_path='report.pdf')
