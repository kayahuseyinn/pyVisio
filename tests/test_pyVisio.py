import unittest
import pyVisio as pv

class TestPyVisio(unittest.TestCase):

    def test_line_chart(self):
        data = [1, 2, 3, 4, 5]
        self.assertIsNone(pv.line_chart(data, title="Line Chart", xlabel="X Axis", ylabel="Y Axis", color='red'))

    def test_bar_chart(self):
        data_bar = {'A': 10, 'B': 20, 'C': 30}
        self.assertIsNone(pv.bar_chart(data_bar, title="Bar Chart", xlabel="Category", ylabel="Value", color='blue'))

    def test_scatter_plot(self):
        x_data = [1, 2, 3, 4, 5]
        y_data = [10, 14, 12, 15, 10]
        self.assertIsNone(pv.scatter_plot(x_data, y_data, title="Scatter Plot", xlabel="X Axis", ylabel="Y Axis", color='blue'))

    def test_pie_chart(self):
        data_pie = {'Apple': 50, 'Pear': 30, 'Cherry': 20}
        self.assertIsNone(pv.pie_chart(data_pie, title="Pie Chart"))

    def test_time_series_analysis(self):
        import numpy as np
        data_ts = np.random.randn(100)
        summary, forecast, anomalies = pv.time_series_analysis(data_ts, detect_anomalies=True)
        self.assertIsNotNone(summary)
        self.assertIsNotNone(forecast)
        self.assertIsNotNone(anomalies)

    def test_generate_report(self):
        report_data = {
            'title': 'Data Analysis Report',
            'author': 'Huseyin Kaya',
            'date': '2024-06-22',
            'content': [
                {'type': 'line_chart', 'data': [1, 2, 3, 4, 5], 'title': 'Line Chart'},
                {'type': 'bar_chart', 'data': {'A': 10, 'B': 20, 'C': 30}, 'title': 'Bar Chart'}
            ]
        }
        self.assertIsNone(pv.generate_report(report_data, format='pdf', output_path='report.pdf'))

    def test_clean_data(self):
        raw_data = {'column1': [1, 2, None, 4, 5], 'column2': [5, None, 3, 2, 1]}
        cleaned_data = pv.clean_data(raw_data, method='fillna', fill_value=0)
        self.assertIsNotNone(cleaned_data)

    def test_set_theme(self):
        custom_theme = {
            'background_color': 'black',
            'grid_color': 'gray',
            'line_color': 'cyan',
            'font_family': 'Arial'
        }
        self.assertIsNone(pv.set_theme(custom_theme))

if __name__ == '__main__':
    unittest.main()
