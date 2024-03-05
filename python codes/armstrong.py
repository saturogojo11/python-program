def is_armstrong(n):
    digits = list(str(n))
    sum_of_digits = sum(int(digit)**len(digits) for digit in digits)
    return sum_of_digits == n

n = 153
print(is_armstrong(n))