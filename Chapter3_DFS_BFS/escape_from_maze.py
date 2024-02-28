from collections import deque

def bfs_search(start, visited, graph):
    queue = deque([start])
    dx = [+1, -1, 0, 0]
    dy = [0, 0, +1, -1]
    while queue:
        start = queue.popleft()
        x, y = start[0], start[1]
        for i in range(4):
            if (x + dx[i] < N and x + dx[i] >= 0) and (y + dy[i] < M and dy[i] + y >= 0) and \
                (graph[x + dx[i]][y + dy[i]] == 1) and (visited[x+dx[i]][y+dy[i]] == 0):
                visited[x + dx[i]][y + dy[i]] = visited[x][y] + 1
                queue.append((x+dx[i], y+dy[i]))
    return visited, graph


# initialization
N, M  = map(int, input().split())
maps = []
dist = []
for i in range(N):
    temp = list(map(str, input()))
    for t in range(len(temp)):
        temp[t] = int(temp[t])
    maps.append(temp)
    dist.append([0 for i in range(len(temp))])

#stage1
start = (0, 0)
dist[start[0]][start[1]] = 1
dist, maps = bfs_search(start, dist, maps)
for l in dist:
    for k in l:
        print("%5d" % k , end=" ")
    print()
print(dist[N-1][M-1])