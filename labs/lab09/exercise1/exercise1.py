import pandas as pd


def explore_data(filename):
    df = pd.read_csv(filename)

    total_student = len(df['StudentID'])
    subjects = ['Math', 'Science', 'English']
    math_avg = float(round(df["Math"].mean(), 1))
    math_highest = df.loc[df['Math'].idxmax(), 'Name']

    result = {
        "total students": total_student,
        "subjects": subjects,
        "math_average": math_avg,
        "highest_math_student": math_highest
    }
    print(result)

explore_data('labs/lab09/data/students.csv')










