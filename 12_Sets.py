# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Displaying sets
print("Set 1:", set1)
print("Set 2:", set2)

# Adding elements
set1.add(6)
print("\nSet 1 after adding 6:", set1)

# Removing elements
set1.remove(2)
print("Set 1 after removing 2:", set1)

# Set Union
union_set = set1.union(set2)
print("\nUnion of Set 1 and Set 2:", union_set)

# Set Intersection
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Set Difference
difference_set = set1.difference(set2)
print("Difference of Set 1 and Set 2 (Set1 - Set2):", difference_set)

# Check membership
print("\nIs 3 in Set 1?", 3 in set1)
print("Is 10 in Set 2?", 10 in set2)

