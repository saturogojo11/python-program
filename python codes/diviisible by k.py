def first_divisible_by_k(numbers, k):
    for num in numbers:
        if num % k == 0:
            return num
    return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(first_divisible_by_k(numbers, k))  