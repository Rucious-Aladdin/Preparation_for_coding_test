from collections import deque
import sys
input = sys.stdin.readline

def topological_sort(graphs, W, indegree, time_table, total_time_table):
    q = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            total_time_table[i] += time_table[i]
    
    while q:
        current_node = q.popleft()
        
        for adj_node in graphs[current_node]:
            indegree[adj_node] -= 1
            
            if total_time_table[current_node] > total_time_table[adj_node]:
                total_time_table[adj_node] = total_time_table[current_node]
            #print(total_time_table)
            if indegree[adj_node] == 0:
                total_time_table[adj_node] += time_table[adj_node]
                q.append(adj_node)
            #print(indegree)
            #print(total_time_table)
        

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time_table = [0] + list(map(int, input().split()))
    total_time_table = [0] * (N + 1)
    graphs = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for i in range(K):
        a, b = map(int, input().split())
        graphs[a].append(b)
        indegree[b] += 1
    W = int(input().strip())
    topological_sort(graphs, W, indegree, time_table, total_time_table)
    print(total_time_table[W])    
        
    