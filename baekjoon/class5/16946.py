from collections import deque

N, M = map(int, input().split())
visited = [[False] * M for i in range(N)]
ans_map = [[0] * M for i in range(N)]
maps = []
starts = []
for i in range(N):
    row = list(input())
    for j in range(M):
        row[j] = int(row[j])
    maps.append(row)
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            starts.append((i, j))
            
def bfs(maps, visited, start, N, M):
    count = 1
    x, y = start
    q = deque([start])
    visited[x][y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    borders = []
    while q:
        
        visited[x][y] = True
        x, y = q.popleft()
        
        for i in range(4):
            adj_x, adj_y = x + dx[i], y + dy[i]
            if 0 <= adj_x < N and 0 <= adj_y < M:
                if (visited[adj_x][adj_y] == False) and (maps[adj_x][adj_y] == 0):
                    q.append((adj_x, adj_y))
                    count += 1
                    visited[adj_x][adj_y] = True
                elif (visited[adj_x][adj_y] == False) and (maps[adj_x][adj_y] == 1):
                    visited[adj_x][adj_y] = True
                    borders.append((adj_x, adj_y))
    return borders, count
    
# 필요한 코드는 준비완료!
for start in starts:
    x, y = start
    if visited[x][y] == False:
        visited[x][y] = True
        borders, count = bfs(maps, visited, start, N, M)
        for x, y in borders:
            visited[x][y] = False
            ans_map[x][y] += count
            
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            ans_map[i][j] += 1
        print(ans_map[i][j] % 10, end="")
    print()