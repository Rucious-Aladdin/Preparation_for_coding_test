import heapq
import sys
input = sys.stdin.readline
heap = []
N = int(input())
for i in range(N):
    cmd = int(input())
    if cmd == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, cmd)
        
    