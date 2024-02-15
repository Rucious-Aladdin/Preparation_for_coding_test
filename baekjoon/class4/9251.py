strings1 = list(input())
strings2 = list(input())

dp = [[0] * (len(strings2) + 1) for i in range(len(strings1) + 1)]

for i in range(1, len(strings1) + 1):
    for j in range(1, len(strings2) + 1):
        if strings1[i - 1] == strings2[j - 1]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1], dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len(strings1)][len(strings2)])