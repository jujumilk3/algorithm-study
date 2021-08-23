def solution(table, languages, preference):
    lang_score_dict = {}
    for lang, score in zip(languages, preference):
        lang_score_dict[lang] = score
    scores = []

    for record in table:
        split = record.split()
        sum_score = 0
        for lang in languages:
            if lang in split:
                score = 6 - split.index(lang)
                sum_score += score * lang_score_dict[lang]
                print(lang, score)
        scores.append(sum_score)

    top_cats = []
    for index, score in enumerate(scores):
        if score == max(scores):
            top_cats.append(table[index].split()[0])
    top_cats.sort()
    return top_cats[0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"],
               [7, 5, 5]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"],
               ["JAVA", "JAVASCRIPT"],
               [7, 5]))

