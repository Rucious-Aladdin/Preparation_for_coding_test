from itertools import combinations
from collections import deque
import copy

# 맵 입력 받기
N, M = map(int, input().split())
maps = []
for i in range(N):
    row = list(map(int, input().split()))
    maps.append(row)
# 반복수행을 위한 map 생성
index_lists = []
# 첫 시작위치 생성
starts = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            starts.append((i, j))
        elif maps[i][j] == 0:
            index_lists.append((i, j))

def bfs(maps, starts):
    q = deque(starts)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            adj_x = x + dx[i]
            adj_y = y + dy[i]
            if 0 <= adj_x < N and 0 <= adj_y < M:
                if maps[adj_x][adj_y] == 0:
                    maps[adj_x][adj_y] = 2
                    q.append((adj_x, adj_y))

# 각 맵의 크기에 따라 3개의 벽을 선택 후 모든 경우에 대해 수행
max_area = 0
for walls in combinations(index_lists, 3):
    temp_maps = copy.deepcopy(maps)
    for wall in walls:
        temp_maps[wall[0]][wall[1]] = 1
    bfs(temp_maps, starts)
    area = 0
    for i in range(N):
        for j in range(M):
            if temp_maps[i][j] == 0:
                area += 1
    if area >= max_area:
        max_area = area
print(max_area)