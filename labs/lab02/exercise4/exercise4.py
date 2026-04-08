# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type == "Electric":
        rate = 2
    elif vehicle_type == "Hybrid" and (hour_24 > 6 and hour_24 < 22):
        rate = 5
    elif vehicle_type == "Hybrid":
        rate = 2
    else:
        rate = 5
    # Return hourly rate based on vehicle and time
    return rate

result = get_hourly_rate("Electric", 5)
print(f"Testing Dynamic Parking Rate: {result}")