
def filter_query_times(times):
    mean = sum(times) / len(times)
    for time in times:
        before_variance = (time - mean)
    variance = (before_variance ** 2) / len(times)
    std_dev = variance ** 0.5
    upper_limit = mean + std_dev
    

    filter = []
    for time in times :
        if time <= upper_limit:
            filter.append(time)
    filter.sort()
    return filter

query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [45, 47, 48, 50, 51, 52]