import pandas as pd
import numpy as np


def test(f):
    df = pd.read_csv(f)
    d = df.groupby("State")
    print(type(d))

if __name__ == "__main__":
    csv_data = "data/SalesJan2009.csv"
    test(csv_data)