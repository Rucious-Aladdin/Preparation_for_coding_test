import sys
input = sys.stdin.readline
M = int(input())
set_a = []
for i in range(M):
    cmds = list(input().strip().split())
    
    if cmds[0] == "add":
        if not cmds[1] in set_a:
            set_a.append(cmds[1])
    elif cmds[0] == "remove":
        if cmds[1] in set_a:
            set_a.remove(cmds[1])
    elif cmds[0] == "check":
        if cmds[1] in set_a:
            print(1)
        else:
            print(0)
    elif cmds[0] == "toggle":
        if cmds[1] in set_a:
            set_a.remove(cmds[1])
        else:
            set_a.append(cmds[1])
    elif cmds[0] == "all":
        set_a = [str(i + 1) for i in range(20)]
    else:
        set_a = []
    print(set_a)
    