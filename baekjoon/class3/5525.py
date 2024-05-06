N = int(input())
M = int(input())
Strings = input()

cur = 0
n_count = 0 
answer = 0
while cur < (M - 1):
    if Strings[cur:cur+3] == "IOI":
        n_count += 1
        cur += 2
        if n_count == N:
            answer += 1
            n_count -= 1
    else:
        cur += 1
        n_count = 0
print(answer)