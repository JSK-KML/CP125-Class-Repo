
def find_bottleneck_index(traceroute):
    max_latency = bottleneck_index = 0
    for i in range(len(traceroute)):
        prev_hop, prev_latency = traceroute[i - 1]
        curr_hop, curr_latency = traceroute[i]
        difference = curr_latency - prev_latency
        if difference > max_latency:
            max_latency = difference
            bottleneck_index = i - 1
    return bottleneck_index


# (hop_number, latency_in_ms)
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  
