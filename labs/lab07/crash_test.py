# WRONG — list as key
# Run this to see the crash, then fix it using tuples

config = {
    [192, 168, 1, 1]: "Router"
}

print(config[[192, 168, 1, 1]])
