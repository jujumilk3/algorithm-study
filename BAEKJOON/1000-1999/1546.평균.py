subject_counter = int(input())
array = []
grade = input()
grade = grade.split()
total_grade = 0

for i in range(subject_counter):
    grade[i] = int(grade[i])

max_grade = max(grade)

for i in range(subject_counter):
    grade[i] = float(grade[i]) / max_grade * 100
    total_grade += grade[i]

avg = total_grade / subject_counter

print("%.2f" % avg)
