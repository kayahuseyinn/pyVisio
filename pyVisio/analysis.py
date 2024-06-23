import numpy as np
import pandas as pd

def basic_analysis(data):
    """
    Perform basic analysis on the data.

    Parameters:
        data (array-like): The data to analyze.

    Returns:
        dict: Basic statistics including mean, median, and standard deviation.
    """
    series = pd.Series(data)
    return {
        'mean': series.mean(),
        'median': series.median(),
        'std_dev': series.std()
    }

def advanced_analysis(data):
    """
    Perform advanced analysis on the data.

    Parameters:
        data (array-like): The data to analyze.

    Returns:
        dict: Advanced statistics including skewness and kurtosis.
    """
    series = pd.Series(data)
    return {
        'skewness': series.skew(),
        'kurtosis': series.kurt()
    }
