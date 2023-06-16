def solution(arr):
    idx = 0
    prev = arr

    while True:
        change = []
        for i in prev:
            if i >= 50 and i % 2 == 0:
                change.append(int(i / 2))
            elif i < 50 and i % 2 == 1:
                change.append(i * 2 + 1)
            else:
                change.append(i)

        if prev == change:
            break
        idx += 1

        prev = change

    return idx
