import time

# 1. Simulating a database of 10 million visitor IDs
print("Generating visitor log...")
# Change this line:
visitors_list = set(range(10_000_000))
print("Log generated.")

# 2. A new visitor arrives (User ID: 9,999,999)
new_visitor = 9_999_999

# 3. Check if they have visited before (Linear Search)
print(f"Checking if Visitor {new_visitor} exists...")
start_time = time.time()

if new_visitor in visitors_list:
    print("Visitor found!")

end_time = time.time()
print(f"List Search Time: {end_time - start_time:.5f} seconds")