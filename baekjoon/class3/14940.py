import sys
from collections import deque

input = sys.stdin.readline
maps = []
N, M = map(int, input().split())
visited = [[False] * M for i in range(N)]
times = [[0] * M for i in range(N)]

start_pos = (0, 0)
for i in range(N):
    lists = list(map(int, input().split()))
    maps.append(lists)
    if 2 in lists:
        y = lists.index(2)
        start_pos = (i, y)


def bfs(start_pos, visited, maps):
    clock = 0
    q = deque([[start_pos, clock]])
    visited[start_pos[0]][start_pos[1]] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        node = q.popleft()
        x, y = node[0]
        clock = node[1]
        times[x][y] = clock
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if not visited[x + dx[i]][y + dy[i]] and maps[x + dx[i]][y + dy[i]] == 1:
                    visited[x + dx[i]][y + dy[i]] = True
                    q.append([(x + dx[i], y + dy[i]), clock + 1])
                    
                    
bfs(start_pos, visited, maps)
times[start_pos[0]][start_pos[1]] = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == False and maps[i][j] == 1:
            times[i][j] = -1

for map in times:
    for coord in map:
        print(coord, end=" ")
    print()