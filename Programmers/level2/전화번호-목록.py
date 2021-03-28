# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)):
#             if i != j and phone_book[i] == phone_book[j][0:len(phone_book[i])]:
#                 answer = False
#                 break
#     return answer
"""
1차시도. 효율성 테스트 통과 실패함.
"""

def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
    return answer


print(solution(['119', '97674223', '1195524421']))
print(solution(['123', '456', '789']))
print(solution(['12', '123', '1235', '567', '88']))
print(solution(['123', '1235', '567', '88', '12']))
