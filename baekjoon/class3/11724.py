import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graphs = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
for i in range(M):
    x, y = map(int, input().split())
    graphs[x].append(y)
    graphs[y].append(x)

#bfs는 시간 초과 ... why?
"""
def bfs(start, graphs, visited):
    q = deque([start])
    while q:
        cur_node = q.popleft()
        visited[cur_node] = True
        for adj_node in graphs[cur_node]:
            if not visited[adj_node]:
                q.append(adj_node)
"""
def dfs(v, graph, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, graphs, visited)
        count += 1
print(count)