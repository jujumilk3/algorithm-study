alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def solution(age):
    return "".join([alphabet[x] for x in list(map(int, list(str(age))))])
