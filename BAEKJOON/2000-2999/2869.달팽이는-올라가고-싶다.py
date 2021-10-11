A, B, V = map(int, input().split())
count = (V - B) / (A - B)
count = count + 1 if count != int(count) else count
print(int(count))
