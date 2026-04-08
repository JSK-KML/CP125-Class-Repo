# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    name1 = open(file1, "r")
    name2 = open(file2, "r")
    outfile = open(output_file, "w")
    names = []
    

    for line in name1:
        name = line
        if name not in names:
            names.append(name)
    name1.close()

    for line in name2:
        name = line
        if name not in names:
            names.append(name)
    name2.close()
    
    names.sort()

    outfile.writelines(names)
    outfile.close()
    return len(names)


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
