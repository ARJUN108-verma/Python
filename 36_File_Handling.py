# File Handling in Python

# 1. Writing to a file (creates the file if it doesn't exist)
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example in Python.\n")
    file.write("This is line 2.\n")

print("File written successfully.")

# 2. Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print("\n--- File Content After Writing ---")
    print(content)

# 3. Appending to the file
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

print("Data appended successfully.")

# 4. Reading the updated file
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("\n--- File Content After Appending ---")
    print(updated_content)
