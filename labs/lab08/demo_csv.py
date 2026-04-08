import csv

records = [
    ["Name", "Score"],
    ["Ali", 85],
    ["Sara", 92],
    ["Ahmad", 78]
]

f = open("labs/lab08/data/output.csv", "w", newline="")
writer = csv.writer(f)
writer.writerows(records)
f.close()