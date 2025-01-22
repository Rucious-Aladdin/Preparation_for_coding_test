from collections import deque

N = int(input())

boards = []
for _ in range(N):
    x = list(map(int, input().split()))
    boards.append(x)

count = 0
s_white = []
s_black = []
for i in range(N):
    for j in range(N):
        if boards[i][j] == 1:
            if (i + j) % 2 == 0:
                s_white.append((i, j))
            else:
                s_black.append((i, j))
                

def check_diagonal(maps, x, y):
    prev_x, prev_y = x, y
    if maps[x][y] == 2:
        return False
    
    # right diagonal
    x, y = prev_x, prev_y
    while True:
        if x >= N or y >= N:
            break
        if maps[x][y] == 2:
            return False
        
        x += 1
        y += 1
    
    x, y = prev_x, prev_y
    while True:
        if x >= N or y < 0:
            break
        if maps[x][y] == 2:
            return False
        x += 1
        y -= 1

    x, y = prev_x, prev_y
    while True:
        if x < 0 or y >= N:
            break
        if maps[x][y] == 2:
            return False
        x -= 1
        y += 1
        
    x, y = prev_x, prev_y
    while True:
        if x < 0 or y < 0:
            break
        if maps[x][y] == 2:
            return False
        x -= 1
        y -= 1
        
    return True


def dfs(maps, pos, count, starts):    
    global max_count

    for i in range(pos, len(starts)):
        x_cur, y_cur = starts[i]
        if check_diagonal(maps, x_cur, y_cur):
            maps[x_cur][y_cur] = 2
            if (count + 1) >= max_count:
                max_count = count + 1
            
            if (i + 1) < len(starts):
                dfs(maps, i+1, count+1, starts)
            maps[x_cur][y_cur] = 1

answer = 0
max_count = 0
dfs(maps=boards, pos=0, count=0, starts=s_white)
answer += max_count

max_count = 0
dfs(maps=boards, pos=0, count=0, starts=s_black)
answer += max_count

print(answer)

"""
백트래킹 문제중에 좀 어려운 편에 속하는 문제.
백과 흑의 비숍은 서로 계산할 필요가 없다는 점까지 이용해야 풀 수 있었다.
또한, count 를 계산위치에 대한 실수가 있었는데, check하고 난뒤에 항상 count를 하는 식으로 써야 정답이 되는 문제.

"""