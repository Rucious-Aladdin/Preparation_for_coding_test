import sys
input = sys.stdin.readline

V, E = map(int, input().split())

parents = [i for i in range(V + 1)]
edges = []
for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key = lambda x : x[2])

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2
        
total_cost = 0
for edge in edges:
    set1 = find(parents, edge[0])
    set2 = find(parents, edge[1])
    if set1 != set2:
        union(parents, set1, set2)
        total_cost += edge[2]

print(total_cost)