def find_at_risk_departments(departments, threshold):
    # TODO: Your code here
    # Hint: use .values() on the inner dict — no nested for loop
    pass


departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}
print(find_at_risk_departments(departments, 65))
