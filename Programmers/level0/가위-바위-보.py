win_mapper = {"2": "0", "0": "5", "5": "2"}


def solution(rsp):
    return "".join([win_mapper[c] for c in rsp])


def solution(rsp):
    return (
        rsp.replace("2", "a").replace("0", "b").replace("5", "c").replace("a", "0").replace("b", "5").replace("c", "2")
    )
