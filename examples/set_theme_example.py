import pyVisio as pv

custom_theme = {
    'background_color': 'black',
    'grid_color': 'gray',
    'line_color': 'cyan',
    'font_family': 'Arial'
}
pv.set_theme(custom_theme)
pv.line_chart([1, 2, 3, 4, 5], title="Line Chart with Custom Theme")
