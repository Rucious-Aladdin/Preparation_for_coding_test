import sys
input = sys.stdin.readline

T = int(input())
probs = []
for i in range(T):
    probs.append(int(input()))
x = [0] * 12
x[1] = 1
x[2] = 2
x[3] = 4

for i in range(4, 12):
    x[i] = x[i - 1] + x[i - 2] + x[i -3]

for prob in probs:
    print(x[prob])