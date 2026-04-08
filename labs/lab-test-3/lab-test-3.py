# Programmer name is MOHAMED FAHRIN BIN MOHAMED MUNEER from class C02.
import csv

# Function 1 to display the latest data in from CSV file and calculate the average height.
def display_calculate_average(filename):
    total_height = count = 0

    f = open(filename, "r+", newline="")
    reader = csv.reader(f)
    header = next(reader)

    print("Display latest Information in CSV:")
    print(header)

    for row in reader:
        print(row)
        total_height += int(row[1])
        count += 1

    average = total_height / count
    print(f"The average height is {average:.2f}\n")
    f.close()

# Function 2 to input a new data and display the updated data in CSV file.
def input_new_data(filename):
    print("Enter a new data.")

    gender = input("Enter gender: ")
    height = int(input("Enter height: "))
    weight = int(input("Enter weight: "))
    bmi = float(input("Enter BMI: "))

    f2 = open(filename, "a+", newline="")
    writer = csv.writer(f2)
    writer.writerow([gender, height, weight, bmi])
    f2.close()
    
    print("Display the updated Information in CSV:")

    f3 = open(filename, "r+", newline="")
    reader = csv.reader(f3)
    for row in reader:
        print(row)

    f3.close()

display_calculate_average("labs/lab-test-3/bmi.csv")
input_new_data("labs/lab-test-3/bmi.csv")