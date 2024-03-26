N = int(input())
MAX_squares = 225
dp = [0] * (50001)

dp[1] = 1

powers = []
for i in range(1, MAX_squares):
    powers.append(i ** 2)

for i in range(2, 50001):
    min_val = 5
    for j in range(1, int(i ** 0.5) + 1):
        if dp[i - j ** 2] < min_val:
            min_val = dp[i - j ** 2]
    dp[i] = min_val + 1

print(dp[N])
    