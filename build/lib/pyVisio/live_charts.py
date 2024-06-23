import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time

def live_line_chart(data, title="Live Line Chart", xlabel="X Axis", ylabel="Y Axis", color='blue'):
    fig = go.FigureWidget()
    fig.add_scatter(y=data, mode='lines', line=dict(color=color))

    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel
    )

    display(fig)
    return fig

def live_bar_chart(data, title="Live Bar Chart", xlabel="Category", ylabel="Value", color='blue'):
    df = pd.DataFrame(list(data.items()), columns=['Category', 'Value'])
    fig = go.FigureWidget()
    fig.add_bar(x=df['Category'], y=df['Value'], marker_color=color)

    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel
    )

    display(fig)
    return fig
