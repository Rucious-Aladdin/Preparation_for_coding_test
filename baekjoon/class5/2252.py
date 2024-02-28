from collections import deque

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topological_sort(graph, indegree, N):
    q = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        print(now, end = " ")
        
        for adj_node in graph[now]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                q.append(adj_node)
                
topological_sort(graph, indegree, N)