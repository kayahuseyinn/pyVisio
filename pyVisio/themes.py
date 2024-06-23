import plotly.io as pio

def set_theme(theme):
    """
    Set the theme for visualizations.

    Parameters:
        theme (dict or str): The theme to set. Can be 'dark', 'light' or a custom dictionary.

    Returns:
        None
    """
    if isinstance(theme, str):
        if theme == 'dark':
            pio.templates.default = "plotly_dark"
        elif theme == 'light':
            pio.templates.default = "plotly_white"
        else:
            raise ValueError("Unsupported theme. Please use 'dark' or 'light'.")
    elif isinstance(theme, dict):
        custom_template = pio.templates["plotly"]
        if "background_color" in theme:
            custom_template.layout.paper_bgcolor = theme["background_color"]
            custom_template.layout.plot_bgcolor = theme["background_color"]
        if "grid_color" in theme:
            custom_template.layout.xaxis.gridcolor = theme["grid_color"]
            custom_template.layout.yaxis.gridcolor = theme["grid_color"]
        if "line_color" in theme:
            custom_template.layout.colorway = [theme["line_color"]]
        if "font_family" in theme:
            custom_template.layout.font.family = theme["font_family"]
        pio.templates["custom_theme"] = custom_template
        pio.templates.default = "custom_theme"
    else:
        raise ValueError("Theme must be either a string ('dark', 'light') or a dictionary.")
