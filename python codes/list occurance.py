from collections import Counter

# Create a sample list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Use Counter to count occurrences of each element in the list
counts = Counter(my_list)

# Print the counts
for element, count in counts.items():
    print(f"{element} occurred {count} times")