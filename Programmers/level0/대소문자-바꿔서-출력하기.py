str = input()
for char in str:
    print(char.upper() if char.islower() else char.lower(), end="")
