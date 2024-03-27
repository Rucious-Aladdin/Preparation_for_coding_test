from collections import deque
import copy
import sys
input = sys.stdin.readline

def D(num):
    return (2 * num) % 10000

def S(num):
    return (num - 1) % 10000

def L(num):
    return num // 1000 + (num % 1000)*10

def R(num):
    return num // 10 + (num % 10) * 1000

T = int(input())
for i in range(T):
    # 이전 노드, 이전명령어(backtracking)
    dp_table = [[-1, " "] for i in range(10000)]
    visited = [False] * 10000
    A, B = map(int, input().split())
    
    q = deque([A])
    functions = [D, S, L, R]
    cmds = ["D", "S", "L", "R"]
    while True:
        current_num = q.popleft()
        visited[current_num] = True
        if current_num == B:
            break
        
        for i, x in enumerate(functions):
            next_num = x(current_num)
            if not visited[next_num]:
                visited[next_num] = True
                q.append(next_num)
                dp_table[next_num][0] = current_num
                dp_table[next_num][1] = cmds[i]
    
    idx = B
    answers = []
    while dp_table[idx][0] != -1:
        answers.append(dp_table[idx][1])
        idx = dp_table[idx][0]
    answers.reverse()
    print("".join(answers))