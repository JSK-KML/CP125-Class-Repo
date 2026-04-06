import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)
    
    averages = df[["Math", "Science", "English"]].mean().round(1)

    result = {
        "Math": float(averages["Math"]),
        "Science": float(averages["Science"]),
        "English": float(averages["English"]),
        "best_subjects": averages.idxmax(),
        "worst_subjects": averages.idxmin()
    }
    print(result)

compare_averages("labs/lab09/data/students.csv")