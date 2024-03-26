N, M = map(int, input().split())

adj_matrix = [[int(1e9)] * (N + 1) for i in range(N + 1)]

for i in range(M):
    pos1, pos2 = map(int, input().split())
    adj_matrix[pos1][pos2] = 1
    adj_matrix[pos2][pos1] = 1

for i in range(1, N + 1):
    adj_matrix[i][i] = 0

# 사이를 지나는 노드가 가장 outer loop에 위치해야한다는점.
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            adj_matrix[a][b] = min(adj_matrix[a][b], adj_matrix[a][k] + adj_matrix[k][b])


candidates = []
for i in range(1, N + 1):
    candidates.append(sum(adj_matrix[i][1:]))
print(candidates.index(min(candidates)) + 1)