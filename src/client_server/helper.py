import pandas as pd


def load_staff_list(filename):
    dfs = pd.read_excel(filename, sheet_name='Sheet1')
    df = pd.DataFrame(dfs, columns=dfs.keys())
    return df
