import heapq

INF = int(1e9)
N, M, C = map(int, input().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (N + 1)

def dijkstra(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))            
        
    return distance

distance = dijkstra(C, distance, graph)

count = 0
max_dist = 0
for d in distance:
    if d != INF and d != 0:
        count += 1
        if max_dist <= d:
            max_dist = d

print(count, max_dist)
        