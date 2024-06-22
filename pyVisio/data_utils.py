# data_utils.py

import pandas as pd

def clean_data(data, method='fillna', fill_value=0):
    df = pd.DataFrame(data)
    if method == 'fillna':
        df = df.fillna(fill_value)
    elif method == 'dropna':
        df = df.dropna()
    return df.to_dict()

def transform_data(data, method='normalize'):
    df = pd.DataFrame(data)
    if method == 'normalize':
        df = (df - df.min()) / (df.max() - df.min())
    return df.to_dict()
