N = int(input())

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 3
dp2 = [0] * (N + 1)
dp2[1] = 1
dp2[2] = 3
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796
    dp2[i] = (dp2[i - 1] + 2 * dp2[i - 2])
"""
for i in range(len(dp2)):
    dp2[i] = dp2[i] % 796796
""" 
print(dp[N])
print(dp2[N])
#모듈러연산의 특징
# (a + b) mod p = (a mod p + b mod p) mod p