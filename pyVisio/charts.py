import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def line_chart(data, title=None, xlabel=None, ylabel=None, color='blue', interactive=False, filters=False, tooltip=False):
    if interactive:
        fig = px.line(x=range(len(data)), y=data, title=title, labels={'x': xlabel, 'y': ylabel})
        if filters:
            fig.update_layout(xaxis_rangeslider_visible=True)
        if tooltip:
            fig.update_traces(hoverinfo="all", hovertemplate="Y: %{y}")
        fig.show()
    else:
        plt.plot(data, color=color)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()

def bar_chart(data, title=None, xlabel=None, ylabel=None, interactive=False, color='blue'):
    if interactive:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=list(data.keys()), y=list(data.values()), marker_color=color))
        fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
        fig.show()
    else:
        plt.figure()
        plt.bar(data.keys(), data.values(), color=color)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()

def scatter_plot(x_data, y_data, title=None, xlabel=None, ylabel=None, interactive=False, color='blue'):
    if interactive:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers', marker=dict(color=color)))
        fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
        fig.show()
    else:
        plt.figure()
        plt.scatter(x_data, y_data, color=color)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()

def pie_chart(data, title=None, interactive=False):
    if interactive:
        fig = go.Figure()
        fig.add_trace(go.Pie(labels=list(data.keys()), values=list(data.values())))
        fig.update_layout(title=title)
        fig.show()
    else:
        plt.figure()
        plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
        if title:
            plt.title(title)
        plt.show()
