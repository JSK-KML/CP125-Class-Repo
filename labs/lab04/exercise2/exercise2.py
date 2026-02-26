# Exercise 2: Grade Calculator
# 
# This program calculates class statistics for student scores.
# However, it contains bugs that cause incorrect output.
#
# Expected output for the test below:
#   Average: 77.7, Passing: 5, Failed: 1
#
# Use the debugger to find and fix the bugs.


def calculate_average(scores):
    total = 0
    for i in range(len(scores)):
        total = total + scores[i]
    return total / len(scores)


def count_passing(scores, passing_mark):
    count = 0
    for i in range(len(scores)):
        if scores[i] >= passing_mark:
            count = count + 1
    return count


def get_class_summary(scores, passing_mark):
    average = calculate_average(scores)
    passing = count_passing(scores, passing_mark)
    failed = len(scores) - passing
    return (average, passing, failed)


# Test
scores = [85, 92, 58, 74, 66, 91]
summary = get_class_summary(scores, 60)
print(f"Average: {summary[0]:.1f}, Passing: {summary[1]}, Failed: {summary[2]}")
