# A list of coordinates (mutable lists)
points = [
    (10, 20),
    (5, 5),
    (10, 20) # Duplicate
]

# Try to remove duplicates using a set
unique_points = set(points)
print(unique_points)