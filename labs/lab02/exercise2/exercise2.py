# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    if tent_capacity > 0:
        tent_cost = math.ceil((participants / tent_capacity)) * tent_price
    else:
        tent_cost = 0
    cost = (meal_price * participants) + tent_cost
    return cost

result = calculate_event_cost(47, 6, 100, 25)
print(f"Testing Camping Logistics: {result:.2f}")













