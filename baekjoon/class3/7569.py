from collections import deque
M, N, H = map(int, input().split())

maps = []
q = deque([])
for i in range(H):
    map_2d = []
    for j in range(N):
        x = list(map(int, input().split()))
        for k, value in enumerate(x):
            if value == 1:
                q.append((i, j ,k, 0))
        map_2d.append(x)
    maps.append(map_2d)
visited = [[[False] * M for i in range(N)] for j in range(H)]

breakFlag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if maps[i][j][k] == 0:
                breakFlag = True
                break
        if breakFlag:
            break
    if breakFlag:
        break
else:
    print(0)
    exit()
    
def bfs(maps, visited, q):
    q = q
    maximum_days = -1
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0 ,0]
    dz = [0, 0, 0, 0, 1, -1]
    while q:
        x, y, z, day = q.popleft()
        visited[x][y][z] = True
        
        if day > maximum_days:
            maximum_days = day
        
        for adj in range(6):
            cur_x, cur_y, cur_z = x + dx[adj], y + dy[adj], z + dz[adj]
            if (0 <= cur_x < H) and (0 <= cur_y < N) and (0 <= cur_z < M):
                if visited[cur_x][cur_y][cur_z] == False and maps[cur_x][cur_y][cur_z] == 0:
                    visited[cur_x][cur_y][cur_z] = True
                    maps[cur_x][cur_y][cur_z] = 1
                    q.append((cur_x, cur_y, cur_z, day + 1))
        
    return maximum_days
        

maximum_days = bfs(maps, visited, q)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if maps[i][j][k] == 0:
                print(-1)
                exit()
else:
    print(maximum_days)
    