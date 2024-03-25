import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
maps = []
visited = [[False] * (M + 1) for i in range(N + 1)]

for i in range(N):
    numbers = [int(num) for num in list(input().strip())]
    maps.append(numbers)

def bfs(maps, visited, start):
    q = deque([])
    start_x, start_y = start
    q.append((start_x - 1, start_y - 1, 1))
    visited[0][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        cur_x, cur_y, clock = q.popleft()
        visited[cur_x][cur_y] = True
        
        if cur_x == N - 1 and cur_y == M - 1:
            return clock
        
        for i in range(4):
            adj_x, adj_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= adj_x < N and 0 <= adj_y < M:
                if not visited[adj_x][adj_y] and maps[adj_x][adj_y] == 1:
                    visited[adj_x][adj_y] = True
                    q.append((adj_x, adj_y, clock+1))

print(bfs(maps, visited, (1, 1)))
        