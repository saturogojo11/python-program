def find_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for i in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

n = int(input("Enter the value of n: "))
primes = find_primes(n)
print("Prime numbers from 1 to n are:", primes)
