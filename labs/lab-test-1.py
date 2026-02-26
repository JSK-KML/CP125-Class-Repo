# Programmer's name: MOHAMED FAHRIN BIN MOHAMED MUNEER, Class: C02
# This program determine a student grade based on their mark and will print the result. 
# The program also use a function to simplify process.

def determine_grade(mark):
    if mark >= 80:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade =  "C"
    elif mark >= 40:
        grade =  "D" 
    else:
        grade = "F"

    print(f"Mark: {mark:.1f}, Grade: {grade}")

mark = int(input("Enter the student's mark: "))
determine_grade(mark)0