import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

visited = [[False] * (M) for i in range(N)]
maps = []
start = (0, 0)
for i in range(N):
    Strings = list(input().strip())
    if "I" in Strings:
        start = (i, Strings.index("I"))
    maps.append(Strings)


def bfs(maps, visited, start):
    person_count = 0
    start_x, start_y = start
    q = deque([(start_x, start_y)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        now_x, now_y = q.popleft()
        visited[now_x][now_y] = True
        
        for i in range(4):
            adj_x = now_x + dx[i]
            adj_y = now_y + dy[i]
            if (0 <= adj_x < N) and (0 <= adj_y < M):
                if not visited[adj_x][adj_y]:
                    if maps[adj_x][adj_y] == "P":
                        person_count += 1  
                    elif maps[adj_x][adj_y] == "X":
                        continue
                    q.append((adj_x, adj_y))
                    visited[adj_x][adj_y] = True
    return person_count

person_count = bfs(maps, visited, start)

if person_count == 0:
    print("TT")
else:
    print(person_count)