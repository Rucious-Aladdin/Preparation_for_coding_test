import sys
sys.setrecursionlimit(10 ** 6)


def postvisit(post, node):
    post.append(node)

def explore(G, v, visited, post):
    visited[v] = True

    for u in G[v]:
        if not visited[u]:
            explore(G, u, visited, post)
    postvisit(post, v)

def r_dfs(G, visited, post):
    for i in range(1, V + 1):
        if not visited[i]:
            explore(G, i, visited, post)
    return post

# ===========================================

def f_dfs(G, visited, post):
    sccs = []
    while post:
        source = post.pop()
        if not visited[source]:
            nodes = []
            explore(G, source, visited, nodes)
            nodes.sort()
            sccs.append(nodes)
    
    sccs.sort(key=lambda x: x[0])
    return sccs

if __name__ == "__main__":
    V, E = list(map(int, input().split()))
    G, GR = [[] for _ in range(V + 1)], [[] for _ in range(V + 1)]

    for i in range(E):
        start, end = list(map(int, input().split()))
        G[start].append(end)
        GR[end].append(start)

    visited_g = [False] * (V + 1)
    visited_r = [False] * (V + 1)
    
    # >> G_R 순회
    r_post = []
    r_post = r_dfs(GR, visited_r, r_post)
    
    # >> G_순회
    sccs = f_dfs(G, visited_g, r_post)

    print(len(sccs))
    for scc in sccs:
        print(*scc, end=" ")
        print("-1")
        