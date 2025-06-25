# Traditional function to add 2 numbers
def add(x, y):
    return x + y

# Lambda function to add 2 numbers
add_lambda = lambda x, y: x + y

# Using both functions
print("Using traditional function:", add(5, 3))
print("Using lambda function:", add_lambda(5, 3))

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squares using lambda and map:", squared)

# Lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda and filter:", even_numbers)

# Lambda with sorted()
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Students sorted by score (descending):", sorted_students)

