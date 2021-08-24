fibonaci_list = [0] * 41


def fibonaci(number):
    global fibonaci_list
    if number == 0:
        fibonaci_list[0] = 0
        return 0
    elif number == 1:
        fibonaci_list[1] = 1
        return 1

    if fibonaci_list[number]:
        return fibonaci_list[number]
    else:
        fibonaci_list[number] = fibonaci(number - 1) + fibonaci(number - 2)
        return fibonaci_list[number]


testcase_count = int(input())
for _ in range(testcase_count):
    input_number = int(input())
    if input_number == 0:
        print("1 0")
    elif input_number == 1:
        print("0 1")
    else:
        fibonaci(input_number)
        print("%d %d" % (fibonaci_list[input_number - 1], fibonaci_list[input_number]))
