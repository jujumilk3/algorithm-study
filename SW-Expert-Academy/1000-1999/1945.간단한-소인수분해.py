case_count = int(input())
primes = [11, 7, 5, 3, 2]

for case_number in range(1, case_count + 1):
    number = int(input())
    prime_used_counts = [0, 0, 0, 0, 0]
    while number > 1:
        for index, prime in enumerate(primes):
            if number % prime == 0:
                number /= prime
                prime_used_counts[index] += 1
                break
    print('#{} {}'.format(case_number, ' '.join(map(str, prime_used_counts[::-1]))))


"""
10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750
"""
