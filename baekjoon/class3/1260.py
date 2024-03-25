from collections import deque

N, M, V = map(int, input().split())
graphs = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
for i in range(M):
    source, dest = map(int, input().split())
    graphs[source].append(dest)
    graphs[dest].append(source)

for i, graph in enumerate(graphs):
    graphs[i] = sorted(graph)

def bfs(graphs, visited, start):
    q = deque([])
    q.append(start)
    answers = []
    
    while q:
        current_node = q.popleft()
        answers.append(current_node)
        visited[current_node] = True
        for adj_node in graphs[current_node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append(adj_node)

    return answers
    
dfs_answer = []
def dfs(graphs, visited, start):
    global dfs_answer
    dfs_answer.append(start)
    visited[start] = True
    for adj_node in graphs[start]:
        if not visited[adj_node]:
            dfs(graphs, visited, adj_node)


dfs(graphs, visited, V)
for node in dfs_answer:
    print(node, end = " ")
visited = [False] * (N + 1)
print()
bfs_answer = bfs(graphs, visited, V)
for node in bfs_answer:
    print(node, end=" ")