import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
E = int(input())

graphs = [[] for i in range(V + 1)]
visited = [False] * (V + 1)

for i in range(E):
    x, y = map(int, input().split())
    graphs[x].append(y)
    graphs[y].append(x)

def bfs(start, visited, graphs):
    queue = deque([start])
    while queue:
        cur_node = queue.popleft()
        visited[cur_node] = True
        for adj_node in graphs[cur_node]:
            if not visited[adj_node]:
                queue.append(adj_node)

bfs(1, visited, graphs)
count = 0
for i, node in enumerate(visited):
    if node and i != 1:
        count += 1
print(count)