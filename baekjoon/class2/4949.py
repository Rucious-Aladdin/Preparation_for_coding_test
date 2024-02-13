import sys
from collections import deque

while True:
    is_success = True
    strings = list(input())
    
    if len(strings) == 1 and strings[0] == ".":
        break
    
    stack = []
    for s in strings:
        if s == "(":
            stack.append(s)
        elif s == ")":
            try:
                cmp = stack.pop()
                if cmp != "(":
                    is_success = False
                    break
            except:
                is_success = False
                break
        elif s == "[":
            stack.append(s)
        elif s == "]":
            try:
                cmp = stack.pop()
                if cmp != "[":
                    is_success = False
                    break
            except:
                is_success = False
                break
    if len(stack) != 0:
        is_success = False
        
    if is_success:
        print("yes")
    else:
        print("no")