def solution(id_list, reports, k):
    answer = [0] * len(id_list)
    report_dict = {reportee: set() for reportee in id_list}
    for report in reports:
        split_report = report.split()
        reporter = split_report[0]
        reportee = split_report[1]
        report_dict[reportee].add(reporter)
    for reporters in report_dict.values():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_list.index(reporter)] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
