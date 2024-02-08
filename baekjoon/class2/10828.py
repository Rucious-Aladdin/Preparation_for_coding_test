from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
stack = deque([])

for i in range(N):
    cmds = list(input().split())
    if cmds[0] ==  "push":
        stack.append(cmds[1])
    elif cmds[0] == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif cmds[0] == "size":
        print(len(stack))
    elif cmds[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        try:
            print(stack[-1])
        except:
            print(-1)