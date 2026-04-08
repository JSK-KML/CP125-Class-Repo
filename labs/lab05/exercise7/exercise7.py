
def find_conflicting_ports(rules):
    port_actions = {}
    conflicts = []

    for rule_id, port, action in rules:
        if port in port_actions:
            if port_actions[port] != action:
                conflicts.append((port, rule_id))
        else:
            port_actions[port] = action

    return sorted(conflicts)

rules = [
    (1, 80, "ALLOW"), 
    (2, 443, "ALLOW"), 
    (3, 80, "BLOCK"),
    (4, 22, "BLOCK"), 
    (5, 443, "BLOCK"), 
    (6, 8080, "ALLOW")
]

result = find_conflicting_ports(rules)
print(f"Conflicts: {result}")

rules2 = [
    (1, 80, "ALLOW"), 
    (2, 80, "ALLOW"), 
    (3, 443, "BLOCK")
]

result2 = find_conflicting_ports(rules2)
print(f"Conflicts: {result2}")

