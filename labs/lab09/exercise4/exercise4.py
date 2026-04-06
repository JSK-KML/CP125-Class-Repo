import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    df = pd.read_csv(filename)

    plt.hist(df['Science'], bins=10)
    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")
    plt.show()
    return len(df)


count = show_science_distribution("labs/lab09/data/students.csv")
print(count) 