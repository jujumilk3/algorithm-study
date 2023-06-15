def solution(n):
    # answer = [[0] * n] * n  # 이렇게 하면 주소가 복사된 2차원 배열들이 생겨서 하나만 넣어도 다들어감.
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
    return answer
