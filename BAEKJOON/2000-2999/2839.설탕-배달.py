sugar = int(input())
number_of_package = 0

while sugar > 0:
    if sugar % 5 != 0:
        sugar -= 3
        if sugar < 0:
            number_of_package = -1
            break
        number_of_package += 1
    elif sugar % 5 == 0:
        number_of_package += 1
        sugar -= 5
    elif sugar % 5 != 0 and sugar % 3 != 0:
        number_of_package = -1

print(number_of_package)
