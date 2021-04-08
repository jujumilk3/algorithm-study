def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer
"""
비슷한 방법으로 접근해봤는데 정답처리가 잘 되지 않아 다른 풀이를 참고하였다.
주어진 정렬을 sort하여 오름차순으로 만든 다음에 가장 가벼운 사람과 가장 무거운 사람의 몸무게를
차례대로 더해가며 limit보다 작거나 같으면 같이 보내고, 무거우면 제일 무거운 사람부터
차례대로 보내는 방식이다.

몸무게 오름차순으로 정렬된 배열에서 i는 ->방향, j는 <-방향으로 진행되면서
보트가 허용하면 보내고, 아니면 j부터 보내고, j가 i를 추월하는 순간
모든 검사가 끝난 것이므로 반복문을 종료한다고 생각하면 쉽다.
쉬운데 왜 난 못풀었을까. 
"""


print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80, 50], 100))
