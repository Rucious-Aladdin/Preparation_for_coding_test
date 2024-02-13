N = int(input())

height_weights = []
for i in range(N):
    height_weights.append(list(map(int, input().split())))

ans = []
for x in height_weights:
    count = 0
    for i in height_weights:
        print(x)
        print(i)
        if x[0] < i[0] and x[1] < i[1]:
            count += 1
    ans.append(count + 1)

for p in ans:
    print(p, end=" ")