import sys

input = sys.stdin.readline

N = int(input())
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N)]
# dp[x][y][z] = 자릿수 x까지 봤을 때, 현재 숫자로 y를 선택한 경우, 비트 z에 해당하는 숫자들을 방문했을 때, 경우의 수
mod = 1000000000
res = 0

for k in range(1, 10):  # 0은 제외하고
    dp[0][k][1 << k] = 1  # 초기 경우의 수는 1 (k를 방문함도 동시에 표시)

for i in range(1, N):  # 각 자릿수에 대해
    for k in range(10):  # 0에서 9까지의 숫자 방문
        for bit in range(1024):  # 이때, 모든 방문 기록 경우의 수를 고려
            # bit | (1 << k) == 이전 방문 기록(bit)에 현재 숫자 방문 기록을 추가(| (1 << k))
            if k - 1 >= 0:
                dp[i][k][bit | (1 << k)] += dp[i - 1][k - 1][bit]
            if k + 1 <= 9:
                dp[i][k][bit | (1 << k)] += dp[i - 1][k + 1][bit]
            dp[i][k][bit | (1 << k)] %= mod


for k in range(10):  # 마지막으로 도착한 숫자 (0~9)
    res += dp[N - 1][k][1023]  # 0부터 9까지 모든 숫자를 방문했을 때, 1111111111(2) = 1023
    res %= mod

print(res)

