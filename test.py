import pandas as pd


def read_xl():
    file_path = r"C:\Users\zero\Desktop\A.xlsx"
    data = pd.read_excel(file_path)
    return data

