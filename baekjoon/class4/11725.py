import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

graphs = [[] for i in range(N + 1)]
prenodes = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(N - 1):
    x, y = map(int, input().split())
    graphs[x].append(y)
    graphs[y].append(x)

def bfs(graphs, prenodes, visited):
    start = 1    
    q = deque([start])
    
    while q:
        pre_node = q.popleft()
        visited[pre_node] = True
        for adj_node in graphs[pre_node]:
            if not visited[adj_node]:
                prenodes[adj_node] = pre_node
                q.append(adj_node)

bfs(graphs, prenodes, visited)
for i, node_num in enumerate(prenodes):
    if i >= 2:
        print(node_num)
            