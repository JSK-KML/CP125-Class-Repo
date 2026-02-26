# Define the function once
def calculate_bill(meal_price):
    tax = meal_price * 0.06  # 6% SST tax
    service_charge = 2.00
    total = meal_price + tax + service_charge
    return total

# Now reuse it for each customer
total1 = calculate_bill(8.50)  # Nasi Lemak
print(f"Customer 1 total: RM{total1:.2f}")

total2 = calculate_bill(3.50)  # Roti Canai
print(f"Customer 2 total: RM{total2:.2f}")

total3 = calculate_bill(7.00)  # Mee Goreng
print(f"Customer 3 total: RM{total3:.2f}")

def add_with_print(a, b):
    result = a + b
    print(result)  # Displays the number on screen

def add_with_return(a, b):
    result = a + b
    return result  # Gives back the number

# Test 1: Using print
x = add_with_print(5, 3)
print(f"x contains: {x}")

# Test 2: Using return
y = add_with_return(5, 3)
print(f"y contains: {y}")

def calculate_discount(price):
    return price * 0.10  # Returns 10% of price

original_price = 100.00
discount_amount = calculate_discount(original_price)
final_price = original_price - discount_amount
print(f"Final price: RM{final_price:.2f}\n\n")

def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

# Now the calculation is defined once and reused
area1 = calculate_circle_area(5)
print(f"Circle 1 (radius 5): Area = {area1:.2f}")

area2 = calculate_circle_area(10)
print(f"Circle 2 (radius 10): Area = {area2:.2f}")

area3 = calculate_circle_area(7)
print(f"Circle 3 (radius 7): Area = {area3:.2f}")






















