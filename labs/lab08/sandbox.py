# Lab 08 Sandbox - Follow along with the lab instructions

# Step 1: The Problem - Data doesn't persist
f = open("labs/lab08/data/scores.txt", "r")
scores = []
for line in f:
    scores.append(int(line.strip()))
f.close()

print("Scores:", scores)

# Try running this program again - scores will be empty!
