import sys
sys.setrecursionlimit(10 ** 6)

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

if __name__ == "__main__":
    V, E = map(int, input().split())

    parents = [i for i in range(V + 1)]
    edges = []
    for i in range(E):
        a, b, cost = map(int, input().split())
        edges.append((a, b, cost))

    edges.sort(key = lambda x : x[2])

    total_cost = 0
    for edge in edges:
        if find(parents, edge[0]) != find(parents, edge[1]):
            union(parents, edge[0], edge[1])
            total_cost += edge[2]

    print(total_cost)