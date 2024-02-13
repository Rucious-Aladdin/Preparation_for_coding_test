from collections import deque

N, K = map(int, input().split())

max_val = 100001

visited = [False] * (2 * max_val + 1)
graphs =[[] for i in range(2 * max_val + 1)]

for i in range(len(graphs)):
    if (i - 1) >= 0:
        graphs[i].append(i - 1)
    if (i + 1) <= 2 * max_val:
        graphs[i].append(i + 1)
    if 2 * i <= 2 * max_val:
        graphs[i].append(2 * i)

def bfs(start, graphs, visited, K):
    clock = 0
    queue = deque([(start, 0)])
    
    while queue:
        pos, clock = queue.popleft()
        visited[pos] = True
        
        if pos == K:
            return clock
        
        for node in graphs[pos]:
            if not visited[node]:
                queue.append((node, clock + 1))

print(bfs(N, graphs, visited, K))