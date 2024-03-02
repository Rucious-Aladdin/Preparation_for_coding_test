from collections import deque
#가수 수/ PD수 받기
N, M = map(int, input().split())

#규칙에 따라 그래프 생성 (가수수, 가수순서1, 가수순서2 ...)
graph = [[] for i in range(N + 1)]
indegree = [0] * (N + 1)
for i in range(M):
    singers_order = list(map(int, input().split()))
    singer_num = singers_order.pop(0)
    for i in range(0, singer_num - 1):
        graph[singers_order[i]].append(singers_order[i + 1])
        indegree[singers_order[i + 1]] += 1

        
#위상정렬 알고리즘 작성
def topological_sort(graph, indegree):
    result = []
    q = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for adj_node in graph[now]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                q.append(adj_node)
    return result

#사이클이 있는지 판별
result = topological_sort(graph, indegree)
if len(result) != N:
    print(0)
else:
    for x in result:
        print(x)