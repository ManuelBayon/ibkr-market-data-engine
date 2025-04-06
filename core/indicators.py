import pandas as pd

def calculate_sma(data: pd.DataFrame, window: int, column: str = "close"):
    return data[column].rolling(window=window).mean()