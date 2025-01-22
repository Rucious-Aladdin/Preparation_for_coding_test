N = int(input())
Q = 1_000_000_000
b_range = 1 << 10
dp_table = [[[0 for _ in range(b_range)] for _ in range(10)] for _ in range(N + 1)]

for i in range(10):
    if i > 0:
        dp_table[1][i][1 << i] = 1
    
for i in range(2, N + 1):
    for j in range(10):
        for k in range(b_range):
            if j == 0:
                dp_table[i][j][k | 1 << j] += dp_table[i - 1][1][k] % Q
            elif 1 <= j <= 8:
                dp_table[i][j][k | 1 << j] += (
                    dp_table[i - 1][j - 1][k] + dp_table[i - 1][j + 1][k]
                ) % Q
            elif j == 9:
                dp_table[i][j][k | 1 << j] += (
                    dp_table[i - 1][j - 1][k]
                ) % Q
            else:
                raise AssertionError("j must be [0, 9]")
answer = 0
for i in range(10):
    answer += dp_table[N][i][1023]
print(answer % Q)
# N = 10 --> 9876543210