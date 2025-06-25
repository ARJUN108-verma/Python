# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Printing the entire list
print("List of fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("orange")
print("After adding 'orange':", fruits)

# Inserting at a specific position
fruits.insert(2, "grape")
print("After inserting 'grape' at index 2:", fruits)

# Removing an element
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Popping the last element
last = fruits.pop()
print("Popped fruit:", last)
print("List after popping:", fruits)

# Sorting the list
fruits.sort()
print("Sorted list:", fruits)

# Reversing the list
fruits.reverse()
print("Reversed list:", fruits)

# Length of the list
print("Total fruits:", len(fruits))

