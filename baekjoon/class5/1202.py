import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewerly_info= []
bags_w_limits = []

for i in range(N):
    w, v = map(int, input().split())
    jewerly_info.append((w, v))
for i in range(K):
    bags_w_limits.append(int(input().strip()))
bags_w_limits.sort()
jewerly_info.sort(key=lambda x : (x[0], x[1]))

bags_order = 0
q = []
total_value = 0
cur_jewerly = 0
while bags_order != K:
    while cur_jewerly < N and bags_order < K:
        weight, value = jewerly_info[cur_jewerly]
        if weight > bags_w_limits[bags_order]:
            break
        else:
            heapq.heappush(q, -value)
        cur_jewerly += 1

    if q: #q가 빈상태에서는 heappop 불가 -> index error 야기
        total_value -= heapq.heappop(q)    
    bags_order += 1
print(total_value)