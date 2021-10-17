students_count = int(input())
students = []
for _ in range(students_count):
    students.append(list(map(int, input().split())))

for student in students:
    number = 1
    for compare in students:
        if student[0] < compare[0] and student[1] < compare[1]:
            number += 1
    print(number, end=' ')
