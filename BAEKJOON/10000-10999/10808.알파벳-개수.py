string = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
usages = [0] * 26
dic = dict()
index = 0
for alpha in alphabets:
    dic[alpha] = index
    dic[alpha.upper()] = index
    index += 1
for char in string:
    usages[dic[char]] += 1
print(' '.join(list(map(str, usages))))
