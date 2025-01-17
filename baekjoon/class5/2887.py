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

def kruskal(maps: list[tuple[int, int, int]], parent):
    maps.sort(key=lambda x: (x[0], x[1], x[2]))
    total = 0

    for edge in maps:
        set1 = find(parent, edge[1])
        set2 = find(parent, edge[2])

        if set1 != set2:
            total += edge[0]
            union(parent, edge[1], edge[2])

    return total

if __name__ == "__main__":
    N = int(input())
    planets = []
    parent = [i for i in range(N)]
    for i in range(N):
        planets.append(list(map(int, input().split())))

    xs = [(planets[i][0],i) for i in range(len(planets))]
    ys = [(planets[i][1],i) for i in range(len(planets))]
    zs = [(planets[i][2],i) for i in range(len(planets))]
    for l in [xs, ys, zs]:
        l.sort(key=lambda x: (x[0], x[1]))

    maps = []


    for ls in [xs, ys, zs]:
        for i in range(N-1):
            cost = ls[i+1][0] - ls[i][0]
            src_v, tgt_v = ls[i][1], ls[i+1][1]
            maps.append((cost, src_v, tgt_v))
    
    print(kruskal(maps, parent))



