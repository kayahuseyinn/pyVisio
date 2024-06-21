import matplotlib.pyplot as plt
import plotly.io as pio

def set_theme(theme):
    if theme == "dark":
        plt.style.use('dark_background')
        pio.templates.default = "plotly_dark"
    elif theme == "light":
        plt.style.use('default')
        pio.templates.default = "plotly_white"
    else:
        raise ValueError("Unsupported theme. Please use 'dark' or 'light'.")
