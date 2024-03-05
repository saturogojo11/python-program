def is_binary(n):
    while n > 0:
        if n % 10 not in (0, 1):
            return False
        n //= 10
    return True

n = 1011
print(is_binary(n))