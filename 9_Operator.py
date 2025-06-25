# Python Program to Demonstrate All Types of Operators

# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)      # Addition
print("a - b =", a - b)      # Subtraction
print("a * b =", a * b)      # Multiplication
print("a / b =", a / b)      # Division
print("a % b =", a % b)      # Modulus
print("a ** b =", a ** b)    # Exponentiation
print("a // b =", a // b)    # Floor division

print("\n")

# 2. Assignment Operators
x = 5
print("Assignment Operators:")
x += 2  # Same as x = x + 2
print("x += 2:", x)
x *= 3  # Same as x = x * 3
print("x *= 3:", x)

print("\n")

# 3. Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)    # Equal to
print("a != b:", a != b)    # Not equal to
print("a > b:", a > b)      # Greater than
print("a < b:", a < b)      # Less than
print("a >= b:", a >= b)    # Greater than or equal to
print("a <= b:", a <= b)    # Less than or equal to

print("\n")

# 4. Logical Operators
p = True
q = False
print("Logical Operators:")
print("p and q:", p and q)  # Logical AND
print("p or q:", p or q)    # Logical OR
print("not p:", not p)      # Logical NOT

print("\n")

# 5. Bitwise Operators
x = 5  # 0b0101
y = 3  # 0b0011
print("Bitwise Operators:")
print("x & y:", x & y)   # AND
print("x | y:", x | y)   # OR
print("x ^ y:", x ^ y)   # XOR
print("~x:", ~x)         # NOT
print("x << 1:", x << 1) # Left shift
print("x >> 1:", x >> 1) # Right shift

print("\n")

# 6. Identity Operators
print("Identity Operators:")
print("x is y:", x is y)
print("x is not y:", x is not y)

print("\n")

# 7. Membership Operators
my_list = [1, 2, 3, 4]
print("Membership Operators:")
print("2 in my_list:", 2 in my_list)
print("5 not in my_list:", 5 not in my_list)

