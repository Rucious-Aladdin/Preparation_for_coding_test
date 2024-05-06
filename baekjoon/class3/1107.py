from itertools import product

N = int(input())
M = int(input())
s1 = set([i for i in range(10)])
if M == 0:
    s2 = set([])
else:
    s2 = set(list(map(int, input().split())))
s1  = list(s1 - s2)
min_val = int(1e9)

k = [1, 10, 100, 1000, 10000, 100000]
for j in range(1, 7):
    for x in product(s1, repeat=j):
        num = 0
        for i, n in enumerate(x):
            num += n * k[i]
        value = abs(num - N) + len(str(num))
        if value < min_val:
            min_val = value

value = abs(100 - N)
if value < min_val:
    print(value)
    exit()
print(min_val)