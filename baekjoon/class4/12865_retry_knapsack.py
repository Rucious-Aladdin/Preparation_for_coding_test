N, K = map(int, input().split())

W_Vs= []
dp = [[0] * (N + 1) for i in range(K + 1)]
for i in range(N):
    w, v = map(int, input().split())
    W_Vs.append((w, v))
W_Vs.sort(key = lambda x : (x[0], x[1]))

for i in range(1, K + 1): #무게
    for j in range(1, N + 1): #물건종류
        w, v = W_Vs[j - 1]
        if w <= i:
            dp[i][j] = max(dp[i][j - 1], dp[i - w][j - 1] + v)
        else:
            dp[i][j] = dp[i][j - 1]

print(dp[-1][-1])
