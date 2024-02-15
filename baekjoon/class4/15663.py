from itertools import permutations

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

answer = []
for perms in permutations(range(N), M):
    xs = [nums[x] for x in perms]
    answer.append(xs)
answer.sort()
temp = [answer[0]]
previous = answer[0]
for i in range(1, len(answer)):
    if answer[i] != previous:
        temp.append(answer[i])
        previous = answer[i]
for ans in temp:
    for n in ans:
        print(n, end= " ")
    print()