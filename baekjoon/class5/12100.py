import copy
from collections import deque
N = int(input())

states = []
max_val = 0
for i in range(N):
    state = list(map(int, input().split()))
    states.append(state)
if N == 1:
    print(states[0][0])
    exit()
    
def get_next_board(states, direction):
    if direction == 0: # 왼쪽으로 붙이는 경우
        for i in range(N):
            temp = []
            for j in range(N):
                if states[i][j] != 0:
                    temp.append(states[i][j])
            len_temp = len(temp)
            start = 0
            index = 0
            while start <= len_temp - 1:
                if start == len_temp - 1:
                    states[i][index] = temp[start]
                    start += 1
                elif temp[start] == temp[start + 1]:
                    states[i][index] = 2 * temp[start]
                    start += 2
                else:
                    states[i][index] = temp[start]
                    start += 1
                index += 1
            while index <= N - 1:
                states[i][index] = 0
                index += 1
        
    elif direction == 1: # 위로 붙이는 경우
        for i in range(N):
            start = 0
            index = 0
            temp = []
            for j in range(N):
                if states[j][i] != 0:
                    temp.append(states[j][i])
            len_temp = len(temp)
            while start <= len_temp - 1:
                if start == len_temp - 1:
                    states[index][i] = temp[start]
                    start += 1
                elif temp[start] == temp[start + 1]:
                    states[index][i] = 2 * temp[start]
                    start += 2
                else:
                    states[index][i] = temp[start]
                    start += 1
                index += 1
            while index <= N - 1:
                states[index][i] = 0
                index += 1
                
    elif direction == 2: # 오른쪽으로 붙이는 경우
        for i in range(N):
            temp = []
            for j in range(N):
                if states[i][j] != 0:
                    temp.append(states[i][j])
            len_temp = len(temp)
            start = len_temp - 1
            index = N - 1
            
            while start >= 0:
                if start == 0:
                    states[i][index] = temp[start]
                    start -= 1
                elif temp[start] == temp[start - 1]:
                    states[i][index] = 2 * temp[start]
                    start -= 2
                else:
                    states[i][index] = temp[start]
                    start -= 1
                index -= 1
            while index >= 0:
                states[i][index] = 0
                index -= 1
    else: #아래로 붙이는 경우
        for i in range(N):
            temp = []
            for j in range(N):
                if states[j][i] != 0:
                    temp.append(states[j][i])
            len_temp = len(temp)
            start = len_temp - 1
            index = N - 1
            
            while start >= 0:
                if start == 0:
                    states[index][i] = temp[start]
                    start -= 1
                elif temp[start] == temp[start - 1]:
                    states[index][i] = 2 * temp[start]
                    start -= 2
                else:
                    states[index][i] = temp[start]
                    start -= 1
                index -= 1
            while index >= 0 :
                states[index][i] = 0
                index -= 1
        pass
    return states

def get_max(states, order):
    global max_val
    if order == 3:
        temp_max = 0
        for row in states:
            row_max = max(row)
            if row_max > temp_max:
                temp_max = row_max
        if temp_max > max_val:
            max_val = temp_max
        return 
    else:
        for i in range(4):
            states_copy = copy.deepcopy(states)
            print("current order %d" % order)
            print("previous state")
            for state in states_copy:
                for s in state:
                    print("%3d" % s, end = " ")
                print()
            print()
            
            states_1 = get_next_board(states_copy, i)
            
            print("next state, direction: %d" % i)
            for state in states_1:
                for s in state:
                    print("%3d" % s, end = " ")
                print()
            print()
            
            get_max(states_1, order + 1)
        
    return

get_max(states, 0)
print(max_val)