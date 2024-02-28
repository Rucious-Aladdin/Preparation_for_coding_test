import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) #(비용, 노드번호)
        #현재노드가 이미 처리된적이 있는 노드이면 무시..
        #
        if distance[now] < dist: #확정이 된 노드인지 아닌지를 구분하는 기준이 이렇게 되는 것임.
        # heapq에서 나온 값이 distance[now]의 값보다 크다면, distance배열을 변경할 필요가 없음. 
            continue
        
        for i in graph[now]: #인접 노드에 대한 연산 수행
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])