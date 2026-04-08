# Programmer's name is Mohamed Fahrin Bin Mohamed Muneer from class C02
# This program will accepts 5 integer input values from the user and is stored in a list
# The program will perform printing, calculate sum, and find the largest number

def number_filtering():
    result = []
    for i in range(5):
       num = int(input(f"Enter number{i+1}: "))
       result.append(num)
       
    print(f"Numbers in ascending order: {sorted(result)}")
    print(f"Summation of all numbers: {sum(result)}")
    print(f"Largest number: {max(result)}")

number_filtering()