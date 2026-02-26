def find_score_range(scores):
    """Find the highest and lowest scores."""
    highest = scores[0]
    lowest = scores[0]
    
    for i in range(1, len(scores)):
        score = scores[i]
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    return (highest, lowest)

test_scores = [72, 85, 90, 68, 95, 78, 88]
result = find_score_range(test_scores)
print(f"Highest: {result[0]}, Lowest: {result[1]}")
# Expected: Highest: 95, Lowest: 68
# Actual:   Highest: 95, Lowest: 88
