# Demonstrate list
my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8]
print("List:")
print(my_list)
print("List with duplicates removed:", list(set(my_list)))

# Demonstrate set
my_set = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8])
print("Set:")
print(my_set)

# Demonstrate tuple
my_tuple = (1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8)
print("Tuple:")
print(my_tuple)

# Demonstrate dictionary
my_dict = {"apple": 3, "banana": 5, "cherry": 7}
print("Dictionary:")
print(my_dict)

# Accessing values in a dictionary
print("Value of 'apple':", my_dict["apple"])

# Adding a new key-value pair to a dictionary
my_dict["orange"] = 4
print("Dictionary after adding 'orange':")
print(my_dict)

# Removing a key-value pair from a dictionary
del my_dict["apple"]
print("Dictionary after removing 'apple':")
print(my_dict)