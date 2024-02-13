from collections import deque
import sys
input = sys.stdin.readline
K = int(input())

sum = 0
stack = deque([])
for i in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
        sum += num
    else:
        sum -= stack.pop()
        
print(sum)