
def move(current, direction):
    next = [current[0], current[1]]
    if (direction == "U"):
        if (current[0] > 1):
            next = [current[0] - 1, current[1]]
    elif(direction == "D"):
        if (current[0] < N):
            next = [current[0] + 1, current[1]]
    elif(direction == "L"):
        if (current[1] > 1):
            next = [current[0], current[1] - 1]
    else:
        if (current[1] < N):
            next = [current[0], current[1] + 1]
    #print(next)
    return next

N = int(input())
strings = input().split() #실수한 부분. 이것만 쳐도 리스트형태로 반환됨.

print(strings)
cur = [1, 1]
for direct in strings:
    cur = move(cur, direct)
    print(cur, direct)
    
print(cur[0], cur[1])
