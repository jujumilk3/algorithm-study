testcase_count = int(input())

for _ in range(testcase_count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (((x1-x2)**2) + ((y1-y2)**2)) ** 0.5  # 원의 방정식. 두 원의 거리
    if distance == 0 and r1 == r2:  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접 or 외접일 때
        print(1)
    elif abs(r1-r2) < distance < r1+r2:  # 두 원이 서로 다른 두 점에서 만났을 때
        print(2)
    else:  # 만나지 않을 때
        print(0)
