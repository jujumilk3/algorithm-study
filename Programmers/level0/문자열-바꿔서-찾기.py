def solution(myString, pat):
    return int(pat in myString.replace("A", "|").replace("B", "A").replace("|", "B"))
