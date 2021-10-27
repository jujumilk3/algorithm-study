def prime_list(n):
    n *= 2
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = False
    return len([i for i in range(2, n) if sieve[i] and n//2 < i])


while True:
    n = int(input())
    if n == 1:
        print(1)
    elif n == 0:
        exit(0)
    else:
        primes = prime_list(n)
        print(primes)
