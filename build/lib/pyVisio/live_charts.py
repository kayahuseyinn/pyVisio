import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import time

class LiveChart:
    def __init__(self, title="Canlı Grafik"):
        self.fig = make_subplots(rows=1, cols=1)
        self.fig.update_layout(title_text=title)
        self.fig.show()

    def update_line_chart(self, x_data, y_data):
        self.fig.data = []  # Var olan veriyi temizle
        self.fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines'))
        self.fig.show()

    def start_live_update(self, update_function, interval=1):
        while True:
            x_data, y_data = update_function()
            self.update_line_chart(x_data, y_data)
            time.sleep(interval)
