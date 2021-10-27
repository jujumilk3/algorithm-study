from math import factorial

N, K = map(int, input().split())
print(int(factorial(N) / (factorial(K) * factorial(N - K))))
