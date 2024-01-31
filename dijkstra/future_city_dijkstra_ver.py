import heapq

INF = int(1e9)
N, M = map(int, input().split())
graph =[[] for i in range(N + 1)]
distance_1K = [INF] * (N + 1)
distance_KX = [INF] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b,1)) #(노드번호, 비용)
    graph[b].append((a,1))

X, K = map(int, input().split())

def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start)) #(비용, 노드번호)
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))
    
    return distance

distance_1K = dijkstra(1, distance_1K)
distance_KX = dijkstra(K, distance_KX)

if (distance_1K[K] == INF) or (distance_KX[X] == INF):
    print("-1")
else:
    print(distance_1K[K] + distance_KX[X])
    
print(distance_1K)
print(distance_KX)