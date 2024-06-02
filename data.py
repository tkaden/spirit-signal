import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

spirits_data = read_csv('spirits.csv')
