N = int(input())
K = int(input())

maps = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

for i in range(N + 2):
    if (i == 0) or (i == N + 1):
        for j in range(N + 2):
            maps[i][j] = 9
    else:
        maps[i][0] = 9
        maps[i][-1] = 9

for apple in range(K):
    x, y = map(int, input().split())
    # apple이 있는 위치는 1로 초기화
    maps[x][y] = 1

L = int(input())
commands = []
for i in range(L):
    time, rotation = input().split()
    commands.append([int(time), rotation])

snake_pos = [[1, 1]]
maps[1][1] = 2
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction_key = 0
clock = 0

def turn(key, command):
    if command == "L":
        if key == 0:
            return 3
        else:
            return key - 1
    if command == "D":
        if key == 3:
            return 0
        else:
            return key + 1
"""
def print_maps(maps):
    for l in maps:
        print(l)
    print()
"""
while True:
    #print_maps(maps)
    if len(commands) > 0:
        if clock == commands[0][0]:
            direction_key = turn(direction_key, commands[0][1])
            commands.pop(0)
    
    dx, dy = directions[direction_key][0], directions[direction_key][1]
    cur_pos = snake_pos[-1]
    
    if (maps[cur_pos[0] + dx][cur_pos[1] + dy] == 0):
        snake_pos.append([cur_pos[0] + dx, cur_pos[1] + dy])
        tail_pos = snake_pos.pop(0)
        
        maps[cur_pos[0] + dx][cur_pos[1] + dy] = 2
        maps[tail_pos[0]][tail_pos[1]] = 0
        
        clock += 1
    elif (maps[cur_pos[0] + dx][cur_pos[1] + dy] == 1):
        snake_pos.append([cur_pos[0] + dx, cur_pos[1] + dy])
        maps[cur_pos[0] + dx][cur_pos[1] + dy] = 2
        
        clock += 1
    else:
        clock += 1
        break
    

print(clock)