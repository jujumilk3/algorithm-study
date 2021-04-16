while True:
    try:
        x = input()
        print(int(x.split()[0]) + int(x.split()[1]))
    except:
        break
