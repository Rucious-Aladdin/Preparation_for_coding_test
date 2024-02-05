import time

strings = list(input())
strings = [int(s) for s in strings]

right = len(strings) - 1
left = 0
count = 0
flag = True

while len(strings) != 0:
    if strings[0] == strings[-1]:
        temp_r = strings[0]
        temp_l = strings[-1]
        while (len(strings) != 0 and temp_r == strings[0]):
            strings.pop(0)
        while (len(strings) != 0 and temp_l == strings[-1]):
            strings.pop()
        if flag:
            flag = False
        else:
            count += 1
    else:
        temp_r = strings[0]
        while (len(strings) != 0 and temp_r == strings[0]):
            strings.pop(0)
        count += 1
    
        
print(count)