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

teams = []
for i in range(N+1):
    teams.append(i)

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union(teams, b, c)
    else:
        if find(teams, b) == find(teams, c):
            print("YES")
        else:
            print("NO")
    
