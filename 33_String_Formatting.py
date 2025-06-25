# Program to show string formatting in Python

name = "Arjun"
age = 22
score = 95.6789

print("=== String Formatting Examples ===")

# 1. Using % operator (Old Style)
print("Old Style: My name is %s and I am %d years old." % (name, age))

# 2. Using str.format() method
print("str.format(): My name is {} and I am {} years old.".format(name, age))
print("Formatted Score: {:.2f}".format(score))  # Limit to 2 decimal places

# 3. Using f-strings (Python 3.6+)
print(f"f-string: My name is {name} and I am {age} years old.")
print(f"My score is {score:.2f}")

# 4. Aligning strings
print("{:<10} {:>10} {:^10}".format("Left", "Right", "Center"))

# 5. Padding numbers with zeros
number = 7
print("Padded number: {:03}".format(number))  # Output: 007

# 6. Formatting with dictionary
person = {"name": "Arjun", "age": 22}
print("Dict format: My name is {name} and I am {age}.".format(**person))

# 7. Using format specifiers with integers
print("Binary: {0:b}, Octal: {0:o}, Hex: {0:x}".format(25))

# End
print("=== End of Examples ===")
