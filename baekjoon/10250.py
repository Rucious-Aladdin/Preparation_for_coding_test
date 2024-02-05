"""
2
6 12 10
30 50 72
"""
M = int(input())
for i in range(M):
    H, W, N = map(int, input().split())
    X = N // H + 1
    Y = N % H
    if Y == 0:
        Y = H
    Y = str(Y)
    if X < 10:
        X = "0" + str(X)
    else:
        X = str(X)
    print(Y + X)