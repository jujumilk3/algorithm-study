def solution(records):
    answer = []
    nickname_list = {}
    for record in records:
        action = record.split()[0]
        uid = record.split()[1]
        nickname = '' if action == 'Leave' else record.split()[2]
        if nickname:
            nickname_list[uid] = nickname
    for record in records:
        action = record.split()[0]
        uid = record.split()[1]
        temp_string = ""
        if action == 'Enter':
            temp_string = nickname_list[uid] + "님이 들어왔습니다."
        elif action == 'Leave':
            temp_string = nickname_list[uid] + "님이 나갔습니다."
        if temp_string:
            answer.append(temp_string)
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
                "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
