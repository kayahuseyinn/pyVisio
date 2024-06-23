
# pyVisio API Reference

## Table of Contents
- [Introduction](#introduction)
- [Functions](#functions)
  - [line_chart](#line_chart)
  - [bar_chart](#bar_chart)
  - [scatter_plot](#scatter_plot)
  - [pie_chart](#pie_chart)
  - [time_series_analysis](#time_series_analysis)
  - [detect_anomalies_in_series](#detect_anomalies_in_series)
  - [clean_data](#clean_data)
  - [set_theme](#set_theme)
  - [live_line_chart](#live_line_chart)
  - [live_bar_chart](#live_bar_chart)
  - [generate_report](#generate_report)
  - [basic_analysis](#basic_analysis)
  - [advanced_analysis](#advanced_analysis)

## Introduction
`pyVisio` is a dynamic and interactive data visualization library that provides comprehensive tools for creating various types of charts, performing data analysis, and generating reports.

## Functions

### line_chart
```python
pv.line_chart(data, title="Line Chart", xlabel="X Axis", ylabel="Y Axis", color='blue', interactive=False)
```
Creates a line chart.

#### Parameters
- **data**: (list) List of numerical values.
- **title**: (str) Title of the chart.
- **xlabel**: (str) Label for the X-axis.
- **ylabel**: (str) Label for the Y-axis.
- **color**: (str) Color of the line.
- **interactive**: (bool) Specifies whether the chart is interactive.

### bar_chart
```python
pv.bar_chart(data, title="Bar Chart", xlabel="Category", ylabel="Value", color='blue', interactive=False)
```
Creates a bar chart.

#### Parameters
- **data**: (dict) Dictionary with categories as keys and numerical values as values.
- **title**: (str) Title of the chart.
- **xlabel**: (str) Label for the X-axis.
- **ylabel**: (str) Label for the Y-axis.
- **color**: (str) Color of the bars.
- **interactive**: (bool) Specifies whether the chart is interactive.

### scatter_plot
```python
pv.scatter_plot(x_data, y_data, title="Scatter Plot", xlabel="X Axis", ylabel="Y Axis", color='blue', interactive=False)
```
Creates a scatter plot.

#### Parameters
- **x_data**: (list) List of numerical values for the X-axis.
- **y_data**: (list) List of numerical values for the Y-axis.
- **title**: (str) Title of the chart.
- **xlabel**: (str) Label for the X-axis.
- **ylabel**: (str) Label for the Y-axis.
- **color**: (str) Color of the points.
- **interactive**: (bool) Specifies whether the chart is interactive.

### pie_chart
```python
pv.pie_chart(data, title="Pie Chart", interactive=False)
```
Creates a pie chart.

#### Parameters
- **data**: (dict) Dictionary with categories as keys and numerical values as values.
- **title**: (str) Title of the chart.
- **interactive**: (bool) Specifies whether the chart is interactive.

### time_series_analysis
```python
pv.time_series_analysis(data, lags=1, detect_anomalies=False, anomaly_threshold=3)
```
Performs time series analysis.

#### Parameters
- **data**: (list or numpy array) Numerical data.
- **lags**: (int) Number of lags to use in the ARIMA model.
- **detect_anomalies**: (bool) Specifies whether to detect anomalies.
- **anomaly_threshold**: (int) Threshold for detecting anomalies.

### detect_anomalies_in_series
```python
pv.detect_anomalies_in_series(data, threshold=3)
```
Detects anomalies in a time series.

#### Parameters
- **data**: (list or numpy array) Numerical data.
- **threshold**: (int) Threshold for detecting anomalies.

### clean_data
```python
pv.clean_data(data, method='fillna', fill_value=0)
```
Cleans the data.

#### Parameters
- **data**: (dict or pandas DataFrame) Data to be cleaned.
- **method**: (str) Method to use for cleaning the data ('fillna', 'dropna').
- **fill_value**: (any) Value to fill NaNs with if 'fillna' method is used.

### set_theme
```python
pv.set_theme(theme)
```
Sets the theme for the charts.

#### Parameters
- **theme**: (dict) Dictionary with keys 'background_color', 'grid_color', 'line_color', 'font_family'.

### live_line_chart
```python
pv.live_line_chart(data, title="Live Line Chart", xlabel="X Axis", ylabel="Y Axis", color='blue')
```
Creates a live line chart.

#### Parameters
- **data**: (list) List of numerical values.
- **title**: (str) Title of the chart.
- **xlabel**: (str) Label for the X-axis.
- **ylabel**: (str) Label for the Y-axis.
- **color**: (str) Color of the line.

### live_bar_chart
```python
pv.live_bar_chart(data, title="Live Bar Chart", xlabel="Category", ylabel="Value", color='blue')
```
Creates a live bar chart.

#### Parameters
- **data**: (dict) Dictionary with categories as keys and numerical values as values.
- **title**: (str) Title of the chart.
- **xlabel**: (str) Label for the X-axis.
- **ylabel**: (str) Label for the Y-axis.
- **color**: (str) Color of the bars.

### generate_report
```python
pv.generate_report(report_data, format='pdf', output_path='report.pdf')
```
Generates a report.

#### Parameters
- **report_data**: (dict) Dictionary with details of the report.
- **format**: (str) Format of the report ('pdf', 'html').
- **output_path**: (str) Path to save the report.

### basic_analysis
```python
pv.basic_analysis(data)
```
Performs basic analysis on the data.

#### Parameters
- **data**: (list) List of numerical values.

### advanced_analysis
```python
pv.advanced_analysis(data)
```
Performs advanced analysis on the data.

#### Parameters
- **data**: (list) List of numerical values.
