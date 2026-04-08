def is_subway_exist(start, end, stops):
    return start and end in stops

def find_index(station, name):
    for i in stations:
        for j in stations:

def count_stops(start, end, stops):
    if not is_subway_exist(start, end, stops):
        return -1
    if start_index < end_index:
        return end_index - start_index
    else:
        return start_index - end_index

stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
is_valid = is_subway_exist("Marina", "Sentosa", stations)
print("Subway exists:", is_valid)
station_stops = count_stops("Marina", "Sentosa", stations)
print("Number of stops:", station_stops)



























