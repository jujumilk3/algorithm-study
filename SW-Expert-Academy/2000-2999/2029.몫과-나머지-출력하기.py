case_count = int(input())

for i in range(1, case_count + 1):
    numbers = list(map(int, input().split()))
    print('#{} {} {}'.format(i, numbers[0] // numbers[1], numbers[0] % numbers[1]))


"""
3   
9 2  
15 6 
369 15        
"""
