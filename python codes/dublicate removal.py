def remove_duplicates(input_list):
    unique_set = set()
    return [x for x in input_list if not (x in unique_set or unique_set.add(x))]

my_list = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9]
new_list = remove_duplicates(my_list)
print(new_list)