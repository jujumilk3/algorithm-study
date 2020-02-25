import sys

input = sys.stdin.readline

case_count = int(input())

for i in range(case_count):
    inputted_number = input().rstrip()
    print(int(inputted_number.split()[0]) + int(inputted_number.split()[1]))
