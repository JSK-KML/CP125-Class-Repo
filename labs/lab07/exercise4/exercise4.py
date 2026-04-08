def apply_upgrade(current, upgrade):
    result = current 
    for key, value in upgrade.items():
        if key in result:
            result[key] = max(result[key], value)  
        else:
            result[key] = value


current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   
