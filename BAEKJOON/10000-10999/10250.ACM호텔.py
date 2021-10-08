test_case_count = int(input())

for test_case in range(test_case_count):
    floors, rooms, guest = map(int, input().split())
    room_number = guest // floors + 1
    floor_number = guest % floors
    if floor_number == 0:
        floor_number = floors
        room_number -= 1
    print(floor_number*100+room_number)
