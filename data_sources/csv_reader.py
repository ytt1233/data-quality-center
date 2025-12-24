import pandas as pd
from config.settings import settings

def read_csv_data(path: str = None):
    path = path or settings.DATA_PATH
    df = pd.read_csv(path)
    return df
