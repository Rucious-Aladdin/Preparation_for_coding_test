import heapq 

N = int(input())

cmd_pipes = []

for i in range(N):
    cmd_pipes.append(int(input()))
    
neg_q = []
pos_q = []

for cmd in cmd_pipes:
    if cmd != 0:
        if cmd > 0:
            heapq.heappush(pos_q, cmd)
        else:
            heapq.heappush(neg_q, -cmd)
    else:
        if (not neg_q) and (not pos_q):
            print(0)
        elif neg_q and (not pos_q):
            print(-heapq.heappop(neg_q))
        elif pos_q and (not neg_q):
            print(heapq.heappop(pos_q))
        else:
            if abs(neg_q[0]) <= pos_q[0]:
                print(-heapq.heappop(neg_q))
            else:
                print(heapq.heappop(pos_q))
            
        