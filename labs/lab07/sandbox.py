student = {
    "name": "Ali",
    "age": 20,
    "course": "Computer Science",
    "grade": "A"
}

# 1. Access by key
print(student["course"])

# 2. Safe access with .get()
print(student.get("phone", "No phone listed"))

# 3. Add a new field
student["email"] = "ali@mail.com"

# 4. Update an existing field
student["grade"] = "A+"

# 5. Delete a field
del student["age"]

# 6. Loop with .items()
for key, value in student.items():
    print(f"{key}: {value}")
