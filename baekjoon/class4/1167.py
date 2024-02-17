import sys
from collections import deque

input = sys.stdin.readline

V = int(input())

length1 = [0 for i in range(V + 1)]
visited1 = [False] * (V + 1)
length2 = [0 for i in range(V + 1)]

tree = [[] for i in range(V + 1)]
for i in range(V):
    infos = list(map(int, input().split()))
    root = infos.pop(0)
    num_nodes = len(infos) // 2
    for j in range(num_nodes):
        tree[root].append((infos[j * 2], infos[j * 2 + 1]))

def bfs(length, root, tree, visited):
    q = deque([root])
    length[root] = 0
    while q:
        cur_node = q.popleft()
        visited[cur_node] = True
        for adj_node in tree[cur_node]:
            if not visited[adj_node[0]]:
                q.append(adj_node[0])
                length[adj_node[0]] = length[cur_node] + adj_node[1]
    
    return length.index(max(length))
    
    

root = 1
end_node1 = bfs(length1, root, tree, visited1)

visited2 = [False] * (V + 1)
end_node2 = bfs(length2, end_node1, tree, visited2)
print(max(length2))