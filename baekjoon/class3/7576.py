import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

maps = []
visited = [[False] * M for i in range(N)]

for i in range(N):
    maps.append(list(map(int, input().split())))

start_positions = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            start_positions.append((i, j))

def bfs(start_positions, maps, visited):
    q = deque([])
    for pos in start_positions:
        q.append(pos)
    while q:
        cur_node = q.popleft()
        x, y = cur_node
        visited[x][y] = True
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            x_pos = x + dx[i]
            y_pos = y + dy[i]
            if 0 <= x_pos < N and 0 <= y_pos < M:
                if (not visited[x_pos][y_pos]) and maps[x_pos][y_pos] == 0:
                    q.append((x_pos, y_pos))
                    maps[x_pos][y_pos] = maps[x][y] + 1

bfs(start_positions, maps, visited)

max = 1
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            max = -1
            break
        if max < maps[i][j]:
            max = maps[i][j]
    if max == -1:
        break

for map in maps:
    print(map)

if max == -1:
    print(-1)
else:
    print(max - 1)