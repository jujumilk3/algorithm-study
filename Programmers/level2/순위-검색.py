# def solution(info, query):
#     answer = []
#     for search in query:
#         search_query = search.split(' and ')
#         language = search_query[0]
#         division = search_query[1]
#         career = search_query[2]
#         food = search_query[3].split()[0]
#         score = search_query[3].split()[1]
#         filtered = []
#         for personal in info:
#             if language == '-':
#                 filtered.append(personal)
#             elif language in personal:
#                 filtered.append(personal)
#         for index, personal in enumerate(filtered):
#             if division != '-' and division not in personal:
#                 filtered[index] = None
#             if career != '-' and career not in personal:
#                 filtered[index] = None
#             if food != '-' and food not in personal:
#                 filtered[index] = None
#             if score != '-' and int(score) > int(personal.split()[-1]):
#                 filtered[index] = None
#         answer.append(len(list(filter(lambda x: x is not None, filtered))))
#     return answer
"""
무식하게 풀어봤다. language는 더하는 filter로 쓰고 그 다음부터는 제거하는 필터로 썼는데 로직은 맞으나
효율성테스트에서 전부 시간초과 뜨더라. 왠지 그럴 것 같았다. 이건 이런식으로 풀라는 문제 같지가 않았으니까.
요행은 없구나 싶었다.
문자열로 두면 조건의 길이를 l, 지원자 정보의 총 길이를 t라고 했을 때 0:l ~ t-l:t까지
검사를 하므로, 심지어는 query식이 들어오는 갯수만큼 검색을 하므로 로직이 굉장히 비효율적이게 된다.
주어진 문자열 자료형을 따로 검색하기 좋게 만들어서 하는 수밖에 없겠구나 하는 생각이 들었다.
"""


# def solution(info, query):
#     answer = []
#     applicants = []
#     for personal in info:
#         divided = personal.split()
#         applicant = {
#             'language': divided[0],
#             'division': divided[1],
#             'career': divided[2],
#             'food': divided[3],
#             'score': int(divided[4])
#         }
#         applicants.append(applicant)
#     for search in query:
#         search_query = search.split(' and ')
#         language = search_query[0]
#         division = search_query[1]
#         career = search_query[2]
#         food = search_query[3].split()[0]
#         score = int(search_query[3].split()[1])
#         filtered = []
#         for applicant in applicants:
#             if language == '-':
#                 filtered.append(applicant)
#             elif language == applicant['language']:
#                 filtered.append(applicant)
#         for index, personal in enumerate(filtered):
#             if division != '-' and personal['division'] != division:
#                 filtered[index] = None
#             if career != '-' and personal['career'] != career:
#                 filtered[index] = None
#             if food != '-' and personal['food'] != food:
#                 filtered[index] = None
#             if score != '-' and personal['score'] < score:
#                 filtered[index] = None
#         answer.append(len(list(filter(lambda x: x is not None, filtered))))
#     return answer
"""
음, dict구조로 바꿔서 해당 key가 들어왔을 때 바로 검사를 진행해도 시간초과가 뜬다.
내가 모르는 뭔가가 있구나 싶어서 다른 사람들의 풀이를 참고해봤다.
"""
from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    applicants = defaultdict(list)
    for personal in info:
        divided = personal.split()
        conditions = divided[:-1]
        score = int(divided[-1])
        for i in range(5):
            for comb in combinations(conditions, i):
                applicants[''.join(comb)].append(score)

    for conditions in applicants:
        applicants[conditions].sort()

    import pprint
    pprint.pprint(applicants)

    for search in query:
        divided = search.split(' ')
        score = int(divided[-1])
        conditions = divided[:-1]
        conditions_as_string = ''.join(conditions).replace('-', '').replace('and', '')
        if conditions_as_string in applicants:
            scores = applicants[conditions_as_string]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer
"""
사실상 풀이 그대로라고 봐도 된다. 기술블로그에 자세히 나와있다.https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
블로그에서도 말하듯이 내가 처음에 시도했던 방법, 조건이 추가될 때마다 검색하는 방법은 시간이 오래걸리니 다른방법을 강구하는게 맞았다.
특히 정답에서 요구하는 것이 합격한 사람의 정보가 아니라 숫자인것을 보면 말이다. 풀이를 보고 나니 모든게 명확해지는 현실.

간단하게 말하자면 지원자들의 정보를 검색 옵션과 결부시켜 그 조건 안에 점수리스트를 담아둔 뒤
어떤 조건이 들어오면 그 점수리스트를 가져와서 이분탐색 후에 조건 점수보다 높은 갯수를 list에 담아서 반환하는 것이다.
점수만 비교하는 이유는 이쯤 되면 다 알겠지만 다른 건 문자열의 일치여부만 검사하면 되는데 숫자는 고저의 차이로 조건이 갈리기 때문이다.

어쩌면 말로만 해서는 잘 이해가 안 갈 수도 있다. 그러니까 첫번째 참가자를 예로 들어보자.
java backend junior pizza 150이라는 조건을 갖고 있다. 점수를 제외하고, 이사람이 걸리는 조건식은 몇개가 있을까?


"""


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
