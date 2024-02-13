import sys
input = sys.stdin.readline
N = int(input())
works = []
for i in range(N):
    works.append(list(map(int, input().split())))

works.sort(key = lambda x : (x[1], x[0]))

count = 0
end_time = 0
for work in works:
    if end_time <= work[0]:
        count += 1
        end_time = work[1]

print(count)