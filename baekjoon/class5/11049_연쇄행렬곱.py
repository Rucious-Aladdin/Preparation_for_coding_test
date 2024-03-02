N = int(input())
dimensions = [0] * (N + 1)

for i in range(N):
    a, b = map(int, input().split())
    dimensions[i], dimensions[i + 1] = a, b
    
dp_table = [[0 for i in range(N)] for i in range(N)]

for s in range(N - 1):
    for i in range(N - s - 1):
        j = i + s + 1
        if s == 0:
            dp_table[i][j] += (dimensions[i] * dimensions[i + 1] * dimensions[i + 2])
        else:
            min_val = int(1e9)
            for k in range(i, j):
                cost = dp_table[i][k] + dp_table[k + 1][j] + (dimensions[i] * dimensions[j + 1] * dimensions[k + 1])
                if cost < min_val:
                    dp_table[i][j] = cost
                    min_val = cost
                #print(i, j, k)

print(dp_table[0][-1])