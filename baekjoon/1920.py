N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
temp = list(map(int, input().split()))
M_list = []
for i in range(M):
    M_list.append([temp[i], i, 0])
M_list = sorted(M_list, key = lambda x : x[0])

N_index = 0
for i in range(M):
    while N_index <= N - 1:
        if (M_list[i][0] == N_list[N_index]):
            M_list[i][2] = 1
            break
        
        if (M_list[i][0] > N_list[N_index]):
            N_index += 1
        elif (M_list[i][0] < N_list[N_index]):
            break       
            
M_list = sorted(M_list, key = lambda x : x[1])
for m in M_list:
    print(m[2])