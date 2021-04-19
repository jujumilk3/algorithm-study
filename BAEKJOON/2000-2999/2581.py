x = int(input())
y = int(input())
y += 1
sieve = [True] * y
m = int(y ** 0.5)
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(i+i, y, i):
            sieve[j] = False
prime_list = [i for i in range(2, y) if sieve[i]]
prime_list = [number for number in prime_list if number >= x]

if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)
