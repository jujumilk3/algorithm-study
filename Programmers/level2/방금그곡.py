def solution(m, musicinfos):
    answer = ''
    m = m * 2
    print(m)
    for music_info in musicinfos:
        print(music_info)
        info_split = music_info.split(',')
        start_time_as_list = list(map(int, info_split[0].split(':')))
        start_time = start_time_as_list[0] * 60 + start_time_as_list[1]
        end_time_as_list = list(map(int, info_split[1].split(':')))
        end_time = end_time_as_list[0] * 60 + end_time_as_list[1]
        print(start_time)
        print(end_time)
        spent_time = end_time - start_time
        print(spent_time)
    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
