import array

# Create an integer array
arr = array.array('i', [10, 20, 30, 40, 50])

# Display the array
print("Original Array:")
for i in arr:
    print(i, end=" ")

# Accessing elements
print("\n\nElement at index 2:", arr[2])

# Inserting an element at index 1
arr.insert(1, 15)
print("\nArray after inserting 15 at index 1:")
for i in arr:
    print(i, end=" ")

# Removing an element
arr.remove(30)
print("\n\nArray after removing 30:")
for i in arr:
    print(i, end=" ")

# Appending an element
arr.append(60)
print("\n\nArray after appending 60:")
for i in arr:
    print(i, end=" ")
