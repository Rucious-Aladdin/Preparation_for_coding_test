import heapq
import sys
input = sys.stdin.readline
INF = 1e9

V, E = map(int, input().split())
start = int(input())
graphs = [[] for i in range(V + 1)]
costs = [INF] * (V + 1)
for i in range(E):
    s, d, c = map(int, input().split())
    graphs[s].append((d, c))

def dijkstra(start, graphs, costs):
    q = []
    heapq.heappush(q, (0, start))
    costs[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > costs[now]:
            print("continue 됨")
            continue
        
        for adj_node in graphs[now]:
            cost = dist + adj_node[1]
            if cost < costs[adj_node[0]]:
                costs[adj_node[0]] = cost
                heapq.heappush(q, (cost, adj_node[0]))

dijkstra(start, graphs, costs)

for i in range(1, V + 1):
    if costs[i] == INF:
        print("INF")
    else:
        print(costs[i])