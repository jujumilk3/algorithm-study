def prime_list(n):
    n = n + 1
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


testcase_count = int(input())
testcase_list = [int(i) for i in input().split()]
maxnumber = max(testcase_list)
primelist_of_max = prime_list(maxnumber)
count_of_prime_numbers = len(set(testcase_list) & set(primelist_of_max))

print(count_of_prime_numbers)
