import sys

def D(num_lists, R_count):
    if not num_lists:
        return [-1]
    elif R_count % 2 == 0:
        num_lists.pop(0)
        return num_lists
    else:
        num_lists.pop()
        return num_lists

def R(num_lists):
    x = [0] * (len(num_lists))
    for i in range(len(num_lists)):
        x[len(num_lists) - i - 1] = num_lists[i]
    return x

TC = int(input())

for i in range(TC):
    cmd_pipe = list(input())
    N = int(input())
    
    num_lists = input()
    if num_lists == "[]":
        num_lists = []
    else:
        num_lists = list(num_lists[1:-1].split(","))
        num_lists = [int(num) for num in num_lists]
    
    R_count = 0
    for cmd in cmd_pipe:
        if cmd == "R":
            R_count += 1
        elif cmd == "D":
            num_lists = D(num_lists, R_count)
            if not num_lists:
                pass
            elif num_lists[0] == -1:
                break
    
    if not num_lists:
        print("[]")
    elif num_lists[0] == -1:
        print("error")
    elif R_count % 2 == 1:
        num_lists = R(num_lists)
        num_lists = [str(num) for num in num_lists]
        print("[" + ",".join(num_lists) + "]")
    else:
        num_lists = [str(num) for num in num_lists]
        print("[" + ",".join(num_lists) + "]")