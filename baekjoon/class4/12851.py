import heapq

N, K = map(int, input().split())
INF = int(1e9)
max_val = 100000
graphs =[[] for i in range(2 * max_val + 1)]
costs = [1e9] * (2 * max_val + 1)
for i in range(len(graphs)):
    if (i - 1) >= 0:
        graphs[i].append((i - 1, 1))
    if (i + 1) <= 2 * max_val:
        graphs[i].append((i + 1, 1))
    if 2 * i <= 2 * max_val:
        graphs[i].append((2 * i, 0))

def dijkstra(start, graphs, costs):
    q = []
    heapq.heappush(q, (0, start))
    costs[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        
        if cost > costs[now]:
            continue
        
        for adj_node in graphs[now]:
            cost = costs[now] + adj_node[1]
            if cost < costs[adj_node[0]]:
                costs[adj_node[0]] = cost
                heapq.heappush(q, (cost, adj_node[0])) #비용, 다음으로 갈노드 번호

dijkstra(N, graphs, costs)
print(costs[K])