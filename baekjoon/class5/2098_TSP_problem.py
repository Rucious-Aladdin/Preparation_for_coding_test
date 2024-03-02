from itertools import combinations

N = int(input())

def comb(n, k):
    product1 = 1
    product2 = 1
    for i in range(n, n - k, -1):
        product1 *= i
    for i in range(k, 0, -1):
        product2 *= i
    
    return product1 // product2

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            matrix[i][j] = int(1e9)
 
subsets_cost = [[[int(1e9)] * N for _ in range(comb(N, i + 1))] for i in range(N)]

dict = {}
subsets_cost[0][0][0] = 0
for s in range(1, N + 1):
    if s == 1:
        for i, S in enumerate(combinations(range(N), s)):
            bit_mask = ["0"] * N
            for b in S:
                bit_mask[b] = "1"
            dict["".join(bit_mask)] = i
    if s != 1:
        for i, S in enumerate(combinations(range(N), s)):
            bit_mask = ["0"] * N
            for b in S:
                bit_mask[b] = "1"
            dict["".join(bit_mask)] = i
            if S[0] == 0:
                subsets_cost[s - 1][dict["".join(bit_mask)]][0] = int(1e9)
                for j in S:
                    min_val = int(1e9)
                    if j != 0:
                        for k in S:
                            if k != j:
                                temp = ["0"] * N
                                for b in S:
                                    temp[b] = "1"
                                temp[j] = "0"
                                cost = subsets_cost[s - 2][dict["".join(temp)]][k] + matrix[k][j]
                                if cost < min_val:
                                    min_val = cost
                        temp = ["0"] * N
                        for b in S:
                            temp[b] = "1"
                        subsets_cost[s - 1][dict["".join(temp)]][j] = min_val
            else:
                break

answers = []
print(min([subsets_cost[-1][-1][j] + matrix[j][0] for j in range(N)]))