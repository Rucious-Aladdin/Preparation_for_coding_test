import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i):
    global answer
    traced.append(i)
    visited[i] = True

    next = graphs[i][0]

    if visited[next]:
        if next in traced:
            crit_idx = traced.index(next)
            answer -= (len(traced) - crit_idx)
    else:
        dfs(next)
    
T = int(input())
for _ in range(T):
    # >> Inputs
    N = int(input())
    selects = [None] + list(map(int, input().split()))
    
    # >> Initialize Graphs
    visited = [False] * (N + 1)
    graphs = [[selects[i]] for i in range(N + 1)]
    graphs[0].pop()
    
    # >> DFS cycle search
    answer = N
    for i in range(1, N + 1):
        if not visited[i]:
            traced = []
            dfs(i)
    print(answer)