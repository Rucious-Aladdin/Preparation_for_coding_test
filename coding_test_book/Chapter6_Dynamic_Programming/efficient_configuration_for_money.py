N, M = map(int, input().split())
papers = []
for i in range(N):
    papers.append(int(input()))
max_l = max(M + 1, max(papers) + 1)
dp = [M + 1] * max_l

#a_m = min(a_(m-n1) + 1, ... ,a_(m-nn) +  1)

for p in papers:
    dp[p] = 1

for i in range(M + 1):
    if (dp[i] != 1):
        min = M + 1
        for p in papers:
            if (i - p >= 1) and (dp[i - p] != M + 1):
                if (dp[i - p] < min):
                    min = dp[i - p] + 1
        dp[i] = min
print(dp)

if (dp[M] == M + 1):
    print(-1)
else:
    print(dp[M])