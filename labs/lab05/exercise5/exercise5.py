
def clean_sessions(pool, sessions, dead_servers):
    alive_sessions = []
    dead_set = set(dead_servers)  
    for server, client in sessions:
        if server not in dead_set:
            alive_sessions.append((server, client))
    return alive_sessions


# Test
pool = ("srv-A", "srv-B", "srv-C", "srv-D")
sessions = [("srv-B", "cli-1"), ("srv-A", "cli-2"), ("srv-C", "cli-3"),
            ("srv-B", "cli-4"), ("srv-D", "cli-5")]
dead = ["srv-B", "srv-D"]

result = clean_sessions(pool, sessions, dead)
print(f"Cleaned Sessions: {result}")
# Expected: [('srv-A', 'cli-2'), ('srv-C', 'cli-3')]
