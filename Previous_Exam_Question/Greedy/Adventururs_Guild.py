N = int(input())
fears = list(map(int, input().split()))

last = 0
sum = 0
fears.sort()

for i in range(N):
    if fears[i] <= (i + 1 - last):
        sum += 1
        last = i + 1

print(sum)