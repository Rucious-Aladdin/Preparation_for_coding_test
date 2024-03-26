import heapq
import sys
input = sys.stdin.readline

TC = int(input())
answers = []
for i in range(TC):
    num_cmd = int(input())
    min_q = []
    max_q = []
    idx_dict ={}
    for i in range(num_cmd):
        cmd, num = input().split()
        num = int(num)
        if cmd == "D":
            if num == -1 and min_q:
                idx_dict[min_q[0][1]] = 0
            elif num == 1 and max_q:
                idx_dict[max_q[0][1]] = 0
        else:
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            idx_dict[i] = 1
        
        while min_q and idx_dict[min_q[0][1]] == 0:
            heapq.heappop(min_q)
        while max_q and idx_dict[max_q[0][1]] == 0:
            heapq.heappop(max_q)
    
    if not min_q:
        print("EMPTY")
    else:
        print(-max_q[0][0], min_q[0][0])