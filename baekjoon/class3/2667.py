N = int(input())

maps = []
starts = []
visited = [[False] * N for i in range(N)]
for i in range(N):
    x = [int(num) for num in list(input())]
    for idx, value in enumerate(x):
        if value == 1:
            starts.append((i, idx))
    maps.append(x)

house_count = -1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(maps, visited, start):
    global house_count
    
    now_x, now_y = start
    visited[now_x][now_y] = True
    if house_count == -1:
        house_count = 1
    else:
        house_count += 1
    
    for i in range(4):
        adj_x = now_x + dx[i]
        adj_y = now_y + dy[i]
        if (0 <= adj_x < N) and (0 <= adj_y < N):
            if maps[adj_x][adj_y] == 1 and (not visited[adj_x][adj_y]):
                visited[adj_x][adj_y] = True
                dfs(maps, visited, (adj_x, adj_y))

candidates = []
for start_pos in starts:
    if not visited[start_pos[0]][start_pos[1]]:
        dfs(maps, visited, (start_pos))
    if house_count != -1:
        candidates.append(house_count)
        house_count = -1

print(len(candidates))
candidates.sort()
for x in candidates:
    print(x)