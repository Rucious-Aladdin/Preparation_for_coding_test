def get_2_or_5_num(num):
    num_2 = 0
    num_5 = 0
    
    while True:
        if (num % 2 == 0) and (num != 0):
            num = num / 2
            num_2 += 1
        else:
            break
    
    while True:
        if (num % 5 == 0) and (num != 0):
            num = num / 5
            num_5 += 1
        else:
            break
    return num_2, num_5

N = int(input())

divider_25 = [0, 0]
for i in range(1, N+1):
    num_2, num_5 = get_2_or_5_num(i)
    divider_25[0] += num_2
    divider_25[1] += num_5

print(min(divider_25))

