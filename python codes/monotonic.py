def is_monotonic(lst):
    return all(x <= y for x, y in zip(lst, lst[1:])) or all(x >= y for x, y in zip(lst, lst[1:]))

# Example usage
lst = [1, 2, 3, 4, 5]
print(is_monotonic(lst))  

lst = [5, 4, 3, 2, 1]
print(is_monotonic(lst))  

lst = [1, 2, 3, 4, 5, 4, 3]
print(is_monotonic(lst))  