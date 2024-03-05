def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 4
        for _ in range(2, n):
            a, b = b, a + b
        return b

n = 7
print(fibonacci(n))