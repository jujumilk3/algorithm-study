case_count = int(input())

for case_number in range(1, case_count + 1):
    N, pd, pg = map(int, input().split())

    def is_chk():
        if pg == 100 or pg == 0:
            if pg != pd:
                return False
        if N >= 100:
            return True
        elif N >= 10 and pd % 10 == 0:
            return True
        else:
            for i in range(N, 0, -1):
                if (i*pd) % 100 == 0:
                    return True
        return False

    if is_chk():
        print('#{} Possible'.format(case_number))
    else:
        print('#{} Broken'.format(case_number))

"""
3
100 1 50
1000 81 83
10 10 100
"""
