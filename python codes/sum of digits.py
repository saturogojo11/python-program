def sum_digits(n):
    return sum(int(digit) for digit in str(n))

n = 12345
print(sum_digits(n))