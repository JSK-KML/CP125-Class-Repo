# Demo: Writing text files

# Write data to file
f = open("labs/lab08/data/report.txt", "w")
f.write("Ali: 85\n")
f.write("Sara: 92\n")
f.write("Ahmad: 78\n")
f.close()

print("Data written to labs/lab08/data/output.txt")

# Read it back to verify
f = open("labs/lab08/data/report.txt", "r")
content = f.read()
print("\nFile contents:")
print(content)
f.close()
