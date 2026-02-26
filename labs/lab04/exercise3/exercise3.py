# Exercise 3: Inventory Tracker
#
# This program tracks inventory and calculates restock costs.
# However, it contains bugs that cause incorrect output.
#
# Expected output for the test below:
#   Total value: $1650.00
#   Low stock (<10): [1, 3]
#   Restock cost: $1500.00
#
# Use the debugger to find and fix the bugs.


def get_total_value(quantities, prices):
    total = 0
    for i in range(len(quantities)):
        total = total + quantities[i] * prices[i]
    return total


def find_low_stock(quantities, threshold):
    low_items = []
    for i in range(len(quantities)):
        if quantities[i] < threshold:
            low_items.append(i)
    return low_items


def calculate_restock_cost(quantities, prices, threshold, restock_qty):
    low_indices = find_low_stock(quantities, threshold)
    total_cost = 0
    for i in range(len(low_indices)):
        index = low_indices[i]
        total_cost = total_cost + prices[index] * restock_qty
    return total_cost


# Test
quantities = [50, 5, 100, 3, 25]
prices = [10.00, 25.00, 5.00, 50.00, 15.00]
print(f"Total value: ${get_total_value(quantities, prices):.2f}")
print(f"Low stock (<10): {find_low_stock(quantities, 10)}")
print(f"Restock cost: ${calculate_restock_cost(quantities, prices, 10, 20):.2f}")
