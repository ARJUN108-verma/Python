# Create a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "course": "Artificial Intelligence",
    "marks": 92
}

# Print the whole dictionary
print("Student Dictionary:")
print(student)

# Access specific values
print("\nStudent Name:", student["name"])
print("Student Course:", student["course"])

# Add a new key-value pair
student["grade"] = "A"

# Update an existing value
student["marks"] = 95

# Delete a key-value pair
del student["age"]

# Print the updated dictionary
print("\nUpdated Student Dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")

