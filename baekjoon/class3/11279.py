import heapq
import sys
input = sys.stdin.readline

N = int(input())

pipeline = []
for i in range(N):
    pipeline.append(int(input()))
    
q = []


for number in pipeline:
    if number == 0:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, -number)
        