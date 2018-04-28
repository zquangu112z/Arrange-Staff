import pandas as pd


def load_staff_list(filename):
    dfs = pd.read_excel(filename, sheet_name=None)
    return dfs
