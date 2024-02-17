import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for i in range(N + 1)]
graph_inv = [[] for i in range(N + 1)]
distance1 = [INF] * (N + 1)
distance2 = [INF] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph_inv[b].append((a, c))

def dijkstra(graph, distance, start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
    
        for adj_node in graph[now]:
            cost = distance[now] + adj_node[1]
            if cost < distance[adj_node[0]]:
                distance[adj_node[0]] = cost
                heapq.heappush(q, (cost, adj_node[0]))

dijkstra(graph, distance1, X)
dijkstra(graph_inv, distance2, X)

for i, e in enumerate(distance2):
    distance1[i] += distance2[i]

max_dist = 0
for x in distance1:
    if x > INF:
        continue
    else:
        if max_dist < x:
            max_dist = x

print(max_dist)