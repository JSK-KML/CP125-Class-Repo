def merge_results(existing, new_results):
    for student, score in new_results:
        if student in existing:
            if score > existing[student]:
                existing[student] = score
        else:
            existing[student] = score
    return existing


def get_passing_students(scores, pass_mark):
    passing = []
    for student in scores:
        if scores[student] >= pass_mark:
            passing.append(scores[student])
    return sorted(passing)


if __name__ == "__main__":
    existing = {"Ali": 85, "Sara": 70}
    new_results = {"Ali": 90, "Ahmad": 60}

    merged = merge_results(existing, new_results)
    print(merged)
    print(get_passing_students(merged, 75))
