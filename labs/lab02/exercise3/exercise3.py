# Lab 02 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
    if name == "Director" and pin == 1122:
        access = True
    elif name == "Security" and pin == 9900:
        access = True
    else:
        access = False
    return access

result = validate_entry("Security", 9900)
print(f"Testing Secure Vault System: {result}")
