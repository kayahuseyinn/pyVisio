import pandas as pd

def analyze_data(data):
    df = pd.DataFrame(data)
    description = df.describe()
    correlation = df.corr()
    return description, correlation
