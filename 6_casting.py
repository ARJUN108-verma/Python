# Implicit Casting (done by Python automatically)
print("=== Implicit Casting ===")
a = 5       # int
b = 2.5     # float
c = a + b   # result will be float
print("Value of a (int):", a)
print("Value of b (float):", b)
print("Result of a + b (float):", c)
print("Type of c:", type(c))

# Explicit Casting (done using casting functions)
print("\n=== Explicit Casting ===")

# int to float
x = 10
y = float(x)
print("Integer x:", x)
print("Float y (from x):", y)

# float to int
f = 9.8
i = int(f)
print("Float f:", f)
print("Integer i (from f):", i)

# string to int
s = "123"
num = int(s)
print("String s:", s)
print("Integer num (from s):", num)

# string to float
sf = "45.67"
num2 = float(sf)
print("String sf:", sf)
print("Float num2 (from sf):", num2)

# int to string
n = 99
str_n = str(n)
print("Integer n:", n)
print("String str_n (from n):", str_n)

