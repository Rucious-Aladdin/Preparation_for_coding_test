import sys
input = sys.stdin.readline

TC = int(input())
INF = int(1e9)
answer = []
for _ in range(TC):
    N, M, W = map(int, input().split()) 
    graph = [[INF] * (N + 1) for i in range(N + 1)]
    for i in range(1, N + 1):
        graph[i][i] = 0

    for _ in range(M):
        S, E, T = map(int, input().split())
        if graph[S][E] > T:
            graph[S][E] = T
        if graph[E][S] > T:
            graph[E][S] = T
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        T = -T
        if graph[S][E] > T:
            graph[S][E] = T
    
    temp = "NO"
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                if graph[a][b] < 0 and a == b:
                    temp = "YES"
                    break
            if temp == "YES":
                break
        if temp == "YES":
            break
    answer.append(temp)

for s in answer:
    print(s)