from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


for perms in permutations(range(N), M):
    for x in perms:
        print(nums[x], end = " ")
    print()
