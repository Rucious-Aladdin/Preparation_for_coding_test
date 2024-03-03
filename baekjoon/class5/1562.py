N = int(input())
Q = 1_000_000_000
dp_table = [[0] * 10 for i in range(N)]
for i in range(10):
    dp_table[0][i] = 1
    
for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp_table[i][j] = dp_table[i - 1][1] % Q
        elif 1 <= j <= 8:
            dp_table[i][j] = (dp_table[i - 1][j - 1] + dp_table[i - 1][j + 1]) % Q
        else:
            dp_table[i][j] = dp_table[i - 1][j - 1] % Q

print(dp_table)

# N = 10 --> 9876543210