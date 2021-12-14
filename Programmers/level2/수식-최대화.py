from itertools import permutations


def calc(op, seq, exp):
    if exp.isdigit():  # 더이상 exp에 연산자가 없으면
        return str(exp)  # 그대로 리턴
    else:  # 현 순위 연산자에 따라 진행
        if op[seq] == "*":
            split_data = exp.split("*")  # 연산자로 쪼갬
            temp = []
            for s in split_data:  # 쪼개진 각 부분에 대해 재귀
                temp.append(calc(op, seq + 1, s))
            return str(eval("*".join(temp)))  # 재귀 실행 결과를 담은 배열에 대해 eval()함수로 계산

        if op[seq] == "+":
            split_data = exp.split("+")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("+".join(temp)))

        if op[seq] == "-":
            split_data = exp.split("-")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("-".join(temp)))


def solution(expression):
    answer = 0
    # 6가지 operation 정의
    operations = list(permutations(['*', '+', '-'], 3))

    for op in operations:  # 정의된 op에 따라 calc 재귀 진행
        result = abs(int(calc(op, 0, expression)))  # 얻어낸 결과값에 대해 절대값 취함.

        if result > answer:  # 기존의 결과값과 비교
            answer = result

    return answer
