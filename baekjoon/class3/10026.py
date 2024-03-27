from collections import deque

N = int(input())

maps = []
for i in range(N):
    maps.append(list(input()))
    

def bfs(maps, visited, start, N):
    start_x, start_y = start
    if visited[start_x][start_y] == True:
        return False
    
    q = deque([(start_x, start_y)])
    target_color = maps[start_x][start_y]
    dx = [1, -1, 0, 0]
    dy = [0 , 0, 1, -1]
    
    while q:
        now_x, now_y = q.popleft()
        visited[now_x][now_y] = True
        
        for i in range(4):
            adj_x = now_x + dx[i]
            adj_y = now_y + dy[i]
            if (0 <= adj_x < N) and (0 <= adj_y < N):
                if not visited[adj_x][adj_y] and maps[adj_x][adj_y] == target_color:
                    q.append((adj_x, adj_y))
                    visited[adj_x][adj_y] = True
    return True

visited = [[False] * N for i in range(N)]
normal_count = 0
for i in range(N):
    for j in range(N):
        if bfs(maps, visited, (i, j), N):
            normal_count += 1

visited = [[False] * N for i in range(N)]
unnormal_count = 0
for i in range(N):
    for j in range(N):
        if maps[i][j] == "R" or maps[i][j] == "G":
            maps[i][j] = "X"
for i in range(N):
    for j in range(N):
        if bfs(maps, visited, (i, j), N):
            unnormal_count += 1
print(normal_count, unnormal_count)