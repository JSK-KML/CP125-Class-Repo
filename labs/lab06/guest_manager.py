guests = {"Alice", "Bob"}

# 1. Adding items
guests.add("Charlie")
guests.update(["David", "Eve"]) # Add multiple from a list

# 2. Removing items
guests.remove("Alice")      # Must exist or CRASH
guests.discard("Zorro")     # Safe removal (no error)

print(f"Final guests: {guests}")