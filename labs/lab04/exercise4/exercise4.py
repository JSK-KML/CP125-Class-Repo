
def analyze_performance(lap_times):
    if len(lap_times) % 2 != 0:
        i = (len(lap_times) // 2) + 1
        avg_1 = sum(lap_times[:i]) / len(lap_times[:i])
        avg_2 = sum(lap_times[i-1:]) / len(lap_times[i-1:])
    else:
        i = len(lap_times) / 2
        avg_1 = sum(lap_times[:i]) / len(lap_times[:i])
        avg_2 = sum(lap_times[i:]) / len(lap_times[:i])

    if avg_2 > avg_1:
        return True
    else:
        return False


# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
