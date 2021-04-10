def solution(info, query):
    answer = []
    for search in query:
        search_query = search.split(' and ')
        # print(search_query)
        language = search_query[0]
        division = search_query[1]
        career = search_query[2]
        food = search_query[3].split()[0]
        score = search_query[3].split()[1]
        print(language, division, career, food, score)
        filtered = []
        for personal in info:
            if language == '-':
                filtered.append(personal)
            elif language in personal:
                filtered.append(personal)
        print(filtered)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
