import pandas as pd


def compare_averages(filename):
    df = pd.read_csv(filename)

    math_avg = float(round(df["Math"].mean(), 1))
    Science_avg = float(round(df["Science"].mean(), 1))
    English_avg = float(round(df["English"].mean(), 1))

    

compare_averages("labs/lab09/data/students.csv")