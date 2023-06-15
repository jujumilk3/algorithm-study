def solution(strArr):
    return [x.lower() if i % 2 == 0 else x.upper() for i, x in enumerate(strArr)]
