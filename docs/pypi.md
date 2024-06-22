
# pyVisio Usage Guide

## Installation

You can install pyVisio via pip:

```bash
pip install pyVisio
```

To install the development version, clone the project and run `pip install -e .`:

```bash
git clone https://github.com/kayahuseyinn/pyVisio.git
cd pyVisio
pip install -e .
```

## Basic Usage

### Line Chart

You can create a line chart using the `line_chart` function.

```python
import pyVisio as pv

data = [1, 2, 3, 4, 5]
pv.line_chart(data, title="Line Chart", xlabel="X Axis", ylabel="Y Axis", color='red')
```

### Interactive Line Chart

To create an interactive line chart, set the `interactive` parameter of the `line_chart` function to `True`.

```python
pv.line_chart(data, title="Interactive Line Chart", xlabel="X Axis", ylabel="Y Axis", interactive=True, color='green')
```

### Bar Chart

You can create a bar chart using the `bar_chart` function.

```python
data_bar = {'A': 10, 'B': 20, 'C': 30}
pv.bar_chart(data_bar, title="Bar Chart", xlabel="Category", ylabel="Value", color='blue')
```

### Interactive Bar Chart

To create an interactive bar chart, set the `interactive` parameter of the `bar_chart` function to `True`.

```python
pv.bar_chart(data_bar, title="Interactive Bar Chart", xlabel="Category", ylabel="Value", interactive=True, color='purple')
```

### Scatter Plot

You can create a scatter plot using the `scatter_plot` function.

```python
x_data = [1, 2, 3, 4, 5]
y_data = [10, 14, 12, 15, 10]
pv.scatter_plot(x_data, y_data, title="Scatter Plot", xlabel="X Axis", ylabel="Y Axis", color='blue')
```

### Interactive Scatter Plot

To create an interactive scatter plot, set the `interactive` parameter of the `scatter_plot` function to `True`.

```python
pv.scatter_plot(x_data, y_data, title="Interactive Scatter Plot", xlabel="X Axis", ylabel="Y Axis", interactive=True, color='orange')
```

### Pie Chart

You can create a pie chart using the `pie_chart` function.

```python
data_pie = {'Apple': 50, 'Pear': 30, 'Cherry': 20}
pv.pie_chart(data_pie, title="Pie Chart")
```

### Interactive Pie Chart

To create an interactive pie chart, set the `interactive` parameter of the `pie_chart` function to `True`.

```python
pv.pie_chart(data_pie, title="Interactive Pie Chart", interactive=True)
```

### Time Series Analysis

You can perform time series analysis using the `time_series_analysis` function.

```python
import pyVisio as pv
import numpy as np

data_ts = np.random.randn(100)
summary, forecast, anomalies = pv.time_series_analysis(data_ts, detect_anomalies=True)
print(summary)
print("Forecast:", forecast)
print("Anomalies:", anomalies)
```

### Anomaly Detection

You can detect anomalies in a time series using the `detect_anomalies_in_series` function.

```python
import pyVisio as pv
import numpy as np

data_ts = np.random.randn(100)
anomalies = pv.detect_anomalies_in_series(data_ts)
print("Anomalies:", anomalies)
```

### Report Generation

You can generate an automatic report using the `generate_report` function.

```python
import pyVisio as pv

report_data = {
    'title': 'Data Analysis Report',
    'author': 'Huseyin Kaya',
    'date': '2024-06-22',
    'content': [
        {'type': 'line_chart', 'data': [1, 2, 3, 4, 5], 'title': 'Line Chart'},
        {'type': 'bar_chart', 'data': {'A': 10, 'B': 20, 'C': 30}, 'title': 'Bar Chart'}
    ]
}
pv.generate_report(report_data, format='pdf', output_path='report.pdf')
```

### Data Cleaning

You can clean data using the `clean_data` function.

```python
import pyVisio as pv

raw_data = {'column1': [1, 2, None, 4, 5], 'column2': [5, None, 3, 2, 1]}
cleaned_data = pv.clean_data(raw_data, method='fillna', fill_value=0)
pv.line_chart(cleaned_data['column1'], title="Line Chart with Cleaned Data")
```

### Setting Themes

You can set the theme of the charts using the `set_theme` function.

```python
import pyVisio as pv

custom_theme = {
    'background_color': 'black',
    'grid_color': 'gray',
    'line_color': 'cyan',
    'font_family': 'Arial'
}
pv.set_theme(custom_theme)
pv.line_chart([1, 2, 3, 4, 5], title="Line Chart with Custom Theme")
```
