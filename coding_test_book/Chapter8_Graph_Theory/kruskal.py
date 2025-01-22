def find_parent(parent, x):
    if x != parent[x]:
        #parent[x] 가 인수인 이유 -> x의 부모노드를 타고 거슬러 올라감.
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    v, e = map(int, input().split())
    parent = [0] * (v + 1)
    
    edges = []
    result = 0
    
    for i in range(1, v + 1):
        parent[i]  = i
    
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
        
    edges.sort()
    
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    print(result)
