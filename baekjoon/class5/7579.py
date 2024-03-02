N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

dp_table = [[0] * (sum(costs) + 1) for i in range(N + 1)]

for i in range(1, len(dp_table)): # i == 앱종류
    for j in range(len(dp_table[0])): # 비용 == j
        if j >= costs[i]:
            dp_table[i][j] = max(dp_table[i - 1][j - costs[i]] + memories[i], dp_table[i - 1][j])
        else:
            dp_table[i][j] = dp_table[i - 1][j] 

for i, l in enumerate(dp_table[-1]):
    if l >= M:
        print(i)
        break