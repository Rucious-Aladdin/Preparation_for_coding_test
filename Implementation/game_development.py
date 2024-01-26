def rotate(direction_list, int_to_direct):
    x = direction_list[0]
    y = direction_list[1]
    
    if (x == 1 and y == 0):
        direct_int = 0
    elif(x == 0 and y == 1):
        direct_int = 1
    elif(x == -1 and y == 0):
        direct_int = 2
    else:
        direct_int = 3
        
    if (direct_int == 0):
        direct_int = 3
    else:
        direct_int -= 1
    return int_to_direct[direct_int]
    

N, M = map(int, input().split())
A, B, direction = map(int, input().split())

matrix = []
check_matrix = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    matrix.append(list(map(int, input().split())))

print(check_matrix)
print(N,M)
print(A, B, direction)
print(matrix)

#stage1
int_to_direct = {0:[1,0], 1:[0,1], 2:[-1,0], 3:[0,-1]}
direction_list = int_to_direct[direction]

while(True):
    check = [1, 1, 1, 1]
    for i in range(4):
        direction_list = rotate(direction_list, int_to_direct)
        dx = direction_list[0]
        dy = direction_list[1]
        if ((matrix[A + dx][B + dy] == 0 and check_matrix[A+dx][B+dy] == 0) and
                ((A + dx >= 0 and A + dx < N) and (B + dy >= 0 and B + dy < M))):
            A += dx
            B += dy
            check_matrix[A][B] = 1
            break
        else:
            check[i] = 0
    print(check)
    if (sum(check) == 0):
        if ((matrix[A - dx][B - dy] == 0) and ((A - dx >= 0 and A - dx < N) and (B - dy >= 0 and B - dy < M))):
            A -= dx
            B -= dy
        else:
            break
    print(A, B)

count = 0
for l in check_matrix:
    count += sum(l)
print(count)
    
            
            
            

