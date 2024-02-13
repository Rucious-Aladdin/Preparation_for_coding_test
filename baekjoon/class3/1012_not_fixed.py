import sys
from collections import deque

def bfs_search(maps, pos):
    y, x = pos
    maps[y][x] = 0
    queue = deque([(y, x)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]    
    while len(queue) != 0:
        cur = queue.popleft()
        y, x = cur
        maps[y][x] = 0
        for i in range(4):
            x_pos = x + dx[i]
            y_pos = y + dy[i]
            if x_pos < M and x_pos >= 0 and y_pos < N and y_pos >= 0:
                if maps[y_pos][x_pos] == 1:
                    queue.append((y_pos, x_pos))
                    #이게 1이여서 작동안했음..
                    maps[y_pos][x_pos] = 1
                
input = sys.stdin.readline
T = int(input())
answer = []
#### T에 대한 반복 수행
for _ in range(T):
    M, N, K = map(int, input().split())

    maps = [[0] * (M) for _ in range(N)]
    count = 0
    for i in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1
        
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                bfs_search(maps, (i, j))
                count += 1

    answer.append(count)

for ans in answer:
    print(ans)