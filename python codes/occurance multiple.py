def count_occurrences(numbers, num):
    return numbers.count(num)

numbers = [3, 6, 9, 3, 6, 9, 9, 3, 6, 6, 9]
occurrences_dict = {}

for num in set(numbers):
    occurrences = count_occurrences(numbers, num)
    occurrences_dict[num] = occurrences

print(occurrences_dict)