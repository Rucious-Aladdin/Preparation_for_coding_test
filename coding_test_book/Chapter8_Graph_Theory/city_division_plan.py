def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

edges = []

for i in range(M):
    node1, node2, cost = map(int, input().split())
    edges.append((cost, node1, node2))

edges = sorted(edges, key=lambda x : (x[0], x[1], x[2]))

parent = [ i for i in range(N + 1)]

max = 0
sum = 0
for i in range(M):
    if find(parent, edges[i][1]) != find(parent, edges[i][2]):
       union(parent, edges[i][1], edges[i][2])
       sum += edges[i][0]
       if edges[i][0] > max:
           max = edges[i][0] 
           
print(sum - max)