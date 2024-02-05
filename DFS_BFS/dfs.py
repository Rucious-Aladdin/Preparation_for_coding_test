def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]: #모든 인접노드에 대해서~
        if not visited[i]: #방문하지 않았다면~
            dfs(graph, i, visited) # 그노드에 대해서 dfs 함수를 호출

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]        

visited = [False] * 9 # 중요한 포인트임. visited 배열은 따로만들어야함.

dfs(graph, 1, visited)