import sys
input = sys.stdin.readline

n = int(input())

scores = []
for i in range(n):
    scores.append(int(input()))
scores.sort()

cut = int(round(n * 0.15, 0))
if n == 0:
    print(0)
else:
    print(int(round(sum(scores[cut:len(scores) - cut]) / (len(scores) - 2*cut), 0)))