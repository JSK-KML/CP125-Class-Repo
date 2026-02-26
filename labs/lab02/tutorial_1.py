import math

def calculate_areas(radius_value):
    pi = math.pi
    answer = pi * radius_value * radius_value
    return answer

print("area 1:", calculate_areas(5))
print("area 2:", calculate_areas(10))
print("area 3:", calculate_areas(7))
print()

# Calculating areas
radius_value = 5
pi_value = 3.14159
answer = pi_value * radius_value * radius_value
print(f"Area 1: {answer}")

radius_value_2 = 10
pi_value_2 = 3.14159
answer_2 = pi_value_2 * radius_value_2 * radius_value_2
print(f"Area 2: {answer_2}")

radius_value_3 = 7
pi_value_3 = 3.14159
answer_3 = pi_value_3 * radius_value_3 * radius_value_3
print(f"Area 3: {answer_3}")
