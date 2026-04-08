
def find_slow_endpoints(api_calls, threshold):
    slow_endpoints = set()
    for endpoint, response_time, status_code in api_calls:
        if response_time > threshold:
            slow_endpoints.add(endpoint)
    return sorted(slow_endpoints)

api_calls = [
    # (endpoint, response_time_ms, status_code)
    ("/login", 45, 200), 
    ("/login", 120, 200), 
    ("/data", 80, 200),
    ("/login", 50, 500),
    ("/data", 95, 200), 
    ("/search", 30, 200),
    ("/health", 150, 200)
]

result = find_slow_endpoints(api_calls, 70)
print(f"Slow endpoints: {result}")
