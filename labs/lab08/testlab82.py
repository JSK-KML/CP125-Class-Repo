# Read
f = open("labs/lab08/data/scores.txt", "r")
lines = f.readlines()
f.close()

# Process
scores = []
for line in lines:
    score = int(line.strip())
    scores.append(score)

average = sum(scores) / len(scores)

# Write
f = open("labs/lab08/data/report.txt", "w")
f.write(f"Average: {average}\n")
f.close()

print(average)