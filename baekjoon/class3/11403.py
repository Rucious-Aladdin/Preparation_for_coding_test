# 데이터 입력 받기
N = int(input())
adj_matrix = []

#인접행렬 생성
for i in range(N):
    x = list(map(int, input().split()))
    adj_matrix.append(x)
for i in range(N):
    for j in range(N):
        if (adj_matrix[i][j] == 0):
            adj_matrix[i][j] = int(1e9)

# 플로이드 워셜 알고리즘 수행
for k in range(N):
    for a in range(N):
        for b in range(N):
            adj_matrix[a][b] = min(adj_matrix[a][b], adj_matrix[a][k] + adj_matrix[k][b])

# 정답 행렬 생성            
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == int(1e9):
            adj_matrix[i][j] = 0
        else:
            adj_matrix[i][j] = 1

# 행렬 출력
for i in range(N):
    print(*adj_matrix[i])   


