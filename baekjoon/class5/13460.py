from collections import deque

N, M = map(int, input().split())

maps = []
for i in range(N):
    row = list(input())
    maps.append(row)

R = [0, 0]; B = [0, 0]
for i in range(N):
    for j in range(M):
        if maps[i][j] == "R":
            R[0], R[1] = i, j
        if maps[i][j] == "B":
            B[0], B[1] = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = []

def move(maps, x, y, dx, dy):
    cnt = 0
    while maps[x + dx][y + dy] != "#" and maps[x][y] != "O":
        x += dx
        y += dy
        cnt +=1
    return x, y, cnt

def bfs(maps, R, B):
    q = deque([(R[0], R[1], B[0], B[1], 0)])
    visited.append((R[0], R[1], B[0], B[1]))
    while q:
        cur = q.popleft()
        count = cur[4]
        for i in range(4):
            r_nx, r_ny, count_r = move(maps, cur[0], cur[1], dx[i], dy[i])
            b_nx, b_ny, count_b = move(maps, cur[2], cur[3], dx[i], dy[i])
            
            if maps[b_nx][b_ny] == "O":
                continue
            
            if maps[r_nx][r_ny] == "O":
                print(count + 1)
                return
            
            if r_nx == b_nx and r_ny == b_ny:
                if count_r > count_b:
                    r_nx -= dx[i]
                    r_ny -= dy[i]
                else:
                    b_nx -= dx[i]
                    b_ny -= dy[i]
            
            if (r_nx, r_ny, b_nx, b_ny) not in visited and count <= 8:
                visited.append((r_nx, r_ny, b_nx, b_ny))
                q.append((r_nx, r_ny, b_nx, b_ny, count + 1))
    print(-1)

bfs(maps, R, B)