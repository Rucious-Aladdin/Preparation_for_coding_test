N, M = map(int, input().split())
nums = list(map(int, input().split()))
N_comb = N * (N - 1) // 2

weights = [0 for i in range(M)]

for num in nums:
    weights[num - 1] += 1

for w in weights:
    if w != 0:
        N_comb -= (w * (w - 1) // 2)

print(N_comb)