# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):

    cost = price_per_liter * ((one_way_km * 2) / km_per_liter)
    if cost <= budget:
        return True
    else:
        return False
    

result = is_budget_sufficient(178, 2, 12, 670)
print(f"Testing Road Trip Budgeter: {result}")
