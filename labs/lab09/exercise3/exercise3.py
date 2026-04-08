import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    df = pd.read_csv(filename)

    plt.plot(df.index, df['Math'])
    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Scores")
    plt.show()
    return len(df)

count = show_math_trend("labs/lab09/data/students.csv")
print(count)