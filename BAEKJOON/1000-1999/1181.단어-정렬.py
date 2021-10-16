words_count = int(input())
words = {input() for _ in range(words_count)}
words = sorted(words, key=lambda x: (len(x), x))

for word in words:
    print(word)
