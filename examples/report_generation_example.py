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
