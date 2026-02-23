import time

# 1 million items
data_list = list(range(1_000_000))
data_dict = {i: True for i in range(1_000_000)}
target = 999_999

# List search
start = time.time()
target in data_list
print(f"List search:  {time.time() - start:.5f}s")

# Dict search
start = time.time()
target in data_dict
print(f"Dict search:  {time.time() - start:.5f}s")
