from collections import deque

T = int(input())
for i in range(T):
    strings = list(input())
    stack = deque([])
    is_success = True
    for s in strings:
        if s == "(":
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                is_success = False
                break
    if len(stack) != 0:
        is_success = False
            
    if is_success:
        print("YES")
    else:
        print("NO")