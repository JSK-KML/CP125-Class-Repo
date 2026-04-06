import pandas as pd


def critical_inventory(filename):
    df = pd.read_csv(filename)
    
    cric_item = (df["StockLevel"] > df["DaysSinceRestock"]) & (df["Science"] > 30)
    

    result = {
        "total_products": len(df),
        "critical_count": ,
        "critical_products":
    }

    return result

result = critical_inventory("labs/lab09/data/inventory.csv")
print(result)
