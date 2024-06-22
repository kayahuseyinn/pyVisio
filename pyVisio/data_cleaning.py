import pandas as pd

def clean_data(data, method='fillna', fill_value=0):
    """
    Cleans the input data using the specified method.

    Parameters:
        data (dict): The data to be cleaned.
        method (str, optional): The cleaning method. Default is 'fillna'.
        fill_value (any, optional): The value to use for filling missing data. Default is 0.

    Returns:
        dict: The cleaned data.
    """
    df = pd.DataFrame(data)
    
    if method == 'fillna':
        df = df.fillna(fill_value)
    elif method == 'dropna':
        df = df.dropna()
    
    return df.to_dict(orient='list')
