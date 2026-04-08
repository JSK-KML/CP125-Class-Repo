import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)
    
    mask = (df["Math"] > 85) & (df["Science"] > 85) & (df["English"] > 85)
    mark = df.loc[mask,"Name"]
    
    result = {
        "count": len(mark),
        "names": set(mark)
    }
    return result

print(high_performers("labs/lab09/data/students.csv"))