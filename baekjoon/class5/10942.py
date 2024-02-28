import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
problems = []

for i in range(M):
    problems.append(list(map(int, input().split())))
dp_table = [[0] * (N) for i in range(N)]

for i in range(N):
    dp_table[i][i] = 1
for i in range(N - 1):
    if nums[i] == nums[i + 1]:
        dp_table[i][i + 1] = 1

for i in range(2, N):
    x = 0
    y = i
    while True:
        if nums[x] == nums[y] and dp_table[x + 1][y - 1] == 1:
            dp_table[x][y] = 1
        x += 1
        y += 1
        if y == N:
            break
    
for x in problems:
    print(dp_table[x[0] - 1][x[1] - 1])
