def process_actions(catalog, actions):
    # TODO: Your code here
    pass



catalog = {
    "978-A": 2,
    "978-B": 0,
    "978-C": 1,
}
actions = [
    ("BORROW", "978-A"),
    ("BORROW", "978-A"),
    ("BORROW", "978-B"),
    ("RETURN", "978-B"),
    ("BORROW", "978-Z"),
]
result = process_actions(catalog, actions)
print(result)
