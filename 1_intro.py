# Introduction to Python

# Printing a message
print("Welcome to Python Programming!")

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Performing some operations
year_of_birth = 2025 - age

# Displaying output
print(f"\nHello, {name}!")
print(f"You are {age} years old.")
print(f"You were probably born in the year {year_of_birth}.")

# Using conditional statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loop example
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

