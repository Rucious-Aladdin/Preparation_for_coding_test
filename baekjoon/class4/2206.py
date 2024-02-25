import sys
from collections import deque

input = sys.stdin.readline

maps = []
N, M = map(int, input().split())

for i in range(N):
    temp = list(input().strip())
    maps.append([int(x) for x in temp])

def bfs(start, maps):
    min_dist = int(1e9)
    penetrate_Flag = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(start, 1, penetrate_Flag)])
    maps[start[0]][start[1]] = 2
    
    while q:
        current_node, dist, penetrate_Flag = q.popleft()
        x, y = current_node
        if x == N - 1 and y == M - 1 and dist < min_dist:
            min_dist = dist
        
        for i in range(4):
            adj_x = x + dx[i]
            adj_y = y + dy[i]
            if 0 <= adj_x < N and 0 <= adj_y < M:
                if maps[adj_x][adj_y] == 0:                
                    q.append(((adj_x, adj_y), dist + 1, penetrate_Flag))
                    if penetrate_Flag:
                        maps[adj_x][adj_y] = 2
                    else:
                        maps[adj_x][adj_y] = 3
                elif maps[adj_x][adj_y] == 3 and penetrate_Flag: #벽을 뚫을수 있고 이미 지나간길
                    q.append(((adj_x, adj_y), dist + 1, penetrate_Flag))
                    maps[adj_x][adj_y] = 2
                elif maps[adj_x][adj_y] == 1 and penetrate_Flag: #벽을 만났을때
                    q.append(((adj_x, adj_y), dist + 1, not penetrate_Flag))
    return min_dist

min_val = bfs((0, 0), maps)
if min_val == int(1e9):
    print(-1)
else:
    print(min_val)