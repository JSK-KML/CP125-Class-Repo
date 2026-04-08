# Demo: Reading text files

# Method 1: Read entire file
print("=== Method 1: read() ===")
f = open("labs/lab08/data/demofile.txt", "r")
content = f.read()
print(content)
print(f"Type: {type(content)}")
f.close()

print("\n=== Method 2: readline() ===")
f = open("labs/lab08/data/demofile.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(f"Line 1: {line1}")
print(f"Line 2: {line2}")
f.close()

print("\n=== Method 3: readlines() ===")
f = open("labs/lab08/data/demofile.txt", "r")
lines = f.readlines()
print(f"All lines: {lines}")
f.close()
