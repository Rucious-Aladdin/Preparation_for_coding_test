import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graphs = [[] for i in range(N + 1)]
costs = [int(1e9)] * (N + 1)

for i in range(M):
    src, dest, cost = map(int, input().split())
    graphs[src].append((dest, cost))
    
start, dest = map(int, input().split())

def dijkstra(graphs, costs, start):
    q = []
    heapq.heappush(q, (0, start))
    costs[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        
        # 이줄 안넣으면 시간초과 남.
        # 현재 node의 cost가 costs[node] 보다 크면
        # adj_node에 있는 비용을 더했을 때 cost + costs[adj_node] >  costs[adj_node] + costs[node]
        # 이는 항상 성립하므로 노드의 비용을 계산할 필요가 없는 것임.
        if cost > costs[node]:
            continue
        
        for adj_info in graphs[node]:
            adj_node, adj_cost = adj_info
            cur_cost = adj_cost + cost
            if cur_cost < costs[adj_node]:
                costs[adj_node] = cur_cost
                heapq.heappush(q, (cur_cost, adj_node))

dijkstra(graphs, costs, start)
print(costs[dest])