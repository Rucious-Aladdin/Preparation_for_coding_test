from collections import deque

N = int(input())
queue = deque([])

for i in range(N):
    cmds = list(input().split())
    if cmds[0] == "push_front":
        queue.appendleft(cmds[1])
    elif cmds[0] == "push_back":
        queue.append(cmds[1])
    elif cmds[0] == "pop_front":
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif cmds[0] == "pop_back":
        try:
            print(queue.pop())
        except:
            print(-1)
    elif cmds[0] == "size":
        print(len(queue))
    elif cmds[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmds[0] == "front":
        try:
            print(queue[0])
        except:
            print(-1)
    else:
        try:
            print(queue[-1])
        except:
            print(-1)