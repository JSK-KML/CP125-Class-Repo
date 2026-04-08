# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

def calculate_order_total(products_file, order_file, output_file):
    product = open(products_file, "r")
    order = open(order_file, "r")
    outfile = open(output_file, "w")
    total = 0.0
    product_dict = {}

    
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function
    pass


# Test your code here
result = calculate_order_total("data/products.csv", "data/order.csv", "data/total.csv")
print(f"Grand total: ${result:.2f}")
