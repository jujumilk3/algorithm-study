char_mapper = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"}


def solution(myString):
    return "".join(["l" if c in char_mapper else c for c in myString])


def solution(myString):
    return myString.translate(str.maketrans("abcdefghijk", "lllllllllll"))
