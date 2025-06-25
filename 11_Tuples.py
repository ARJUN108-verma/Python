# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Display the tuple
print("Tuple:", my_tuple)

# Accessing elements by index
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])

# Slicing the tuple
print("Slice [1:]:", my_tuple[1:])

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# Length of tuple
print("Length of my_tuple:", len(my_tuple))

# Check for membership
print("Is 'banana' in my_tuple?", "banana" in my_tuple)

# Loop through a tuple
print("Looping through my_tuple:")
for item in my_tuple:
    print("-", item)

# Tuple unpacking
a, b, c = my_tuple
print("Unpacked values:", a, b, c)

