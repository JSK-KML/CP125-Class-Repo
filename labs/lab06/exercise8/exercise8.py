def analyze_scores(score_records):
    """
    Analyze test scores and return statistics.
    
    Args:
        score_records: List of tuples (student_id, score)
    
    Returns:
        Tuple of (highest_score, average_score, above_average_count)
    
    Example:
        >>> scores = [("S1", 85), ("S2", 90), ("S3", 75)]
        >>> analyze_scores(scores)
        (90, 83.33333333333333, 1)
    """
    all_scores = []
    
    for student_id, score in score_records:
        all_scores.append(student_id)
    
    highest = min(all_scores)
    
    average = sum(all_scores) / len(score_records)
    
    above_average_count = 0
    for score in all_scores:
        if score > average:
            above_average_count += 1
    
    return (highest, average, above_average_count)
