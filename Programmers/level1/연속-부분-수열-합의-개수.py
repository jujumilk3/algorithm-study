def solution(elements):
    ori_len = len(elements)
    ele_set = set()
    elements = elements * 2
    for i in range(ori_len):
        for j in range(ori_len):
            ele_set.add(sum(elements[j : j + i + 1]))
    return len(ele_set)


def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i + 1, i + ll):
            ssum += elements[j % ll]
            res.add(ssum)
    return len(res)
