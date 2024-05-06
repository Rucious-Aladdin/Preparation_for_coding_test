from itertools import combinations_with_replacement

N, M = map(int, input().split())

arr = [i + 1 for i in range(N)]

for comb_tuple in combinations_with_replacement(arr, M):
    for i in range(len(comb_tuple)):
        print(comb_tuple[i], end= " ")
    print()