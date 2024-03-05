def find_min_max(n):
    nums = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)
    min_num = min(nums)
    max_num = max(nums)
    return min_num, max_num

n = int(input("Enter the number of numbers: "))
min_num, max_num = find_min_max(n)
print(f"Minimum: {min_num}")
print(f"Maximum: {max_num}")