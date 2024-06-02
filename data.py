import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path, dtype={"zipcode": str})

if __name__ == "__main__":
    spirits_data = read_csv('spirits.csv')
    print(spirits_data)
