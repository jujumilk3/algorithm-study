def solution(n, left, right):
    # 첫번째실패
    # matrix = [[0 for _ in range(n)] for _ in range(n)]
    # for number in range(1, n+1):
    #     for col in range(number):
    #         for row in range(number):
    #             matrix[col][row] = number if matrix[col][row] == 0 else matrix[col][row]
    # 색칠하는데 다소 비효율적인 로직이라 시간초과나는줄

    # 두번째실패
    # flat = []
    # matrix = []
    # n_list = list(range(1, n+1))
    # for index in n_list:
    #     temp_list = n_list[index:]
    #     numbers = [index] * index
    #     matrix.append(numbers + temp_list)
    #
    # for row in matrix:
    #     flat += row
    # return flat[left:right+1]
    # 로직을 색칠하는 로직을 개선했는데도 시간초과가 뜸. 그래서 그냥 return [1,2,3,4]해도
    # 시간초과가 떠서 애초에 문제의도가 저렇게 배열을 만들면 안되는 것으로 확인.
    # 수학적으로 규칙을 찾아서 풀엉야 함.

    # (0,0) 이면 1, 인덱스에 1이 한개라도 들어가면 2, 인덱스에 2가 하나라도 들어간 곳은 3이다.
    # 이걸 1차원화 해보면 두 index의 몫 혹은 나머지값이 해당 위치의 value라는 것을 알 수 있음.

    answer = []
    for number in range(int(left), int(right)+1):
        quotient, remainder = divmod(number, n)
        answer.append(quotient + 1 if quotient > remainder else remainder + 1)
    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))

