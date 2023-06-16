def solution(date1, date2):
    date1_str = "".join([str(x).zfill(2) for x in date1])
    date2_str = "".join([str(x).zfill(2) for x in date2])
    return int(date1_str < date2_str)


def solution(date1, date2):
    return int(date1 < date2)
