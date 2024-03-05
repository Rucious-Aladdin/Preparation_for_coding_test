import sys
from collections import deque
input = sys.stdin.readline
TC = int(input())
answers = []
for _ in range(TC):
    # 입력받기
    h, w = map(int, input().split())
    maps = []
    keys = []
    visited = [[False] * w for i in range(h)]
    doc_count = 0
    Q = deque([])
    doors = deque([])
    for i in range(h):    
        rows = list(input().strip())
        maps.append(rows)
        if i == 0 or i == h - 1:
            for x in range(len(rows)):
                if rows[x] != "*":
                    if rows[x] == ".":
                        Q.append((i, x))
                    elif rows[x] == "$":
                        doc_count += 1
                        Q.append((i, x))
                    elif ord("a") <= ord(rows[x]) < ord("z"):
                        Q.append((i, x))
                        keys.append(rows[x])
                    else:
                        doors.append((rows[x].lower(), i, x))
                visited[i][x] = True
        else:
            if rows[0] != "*":
                if rows[0] == ".":
                    Q.append((i, 0))
                elif rows[0] == "$":
                    doc_count += 1
                    Q.append((i, 0))
                elif ord("a") <= ord(rows[0]) < ord("z"):
                    Q.append((i, 0))
                    keys.append(rows[0])
                else:
                    doors.append((rows[0].lower(), i, 0))
            if rows[-1] != "*":
                if rows[-1] == ".":
                    Q.append((i, w - 1))
                elif rows[-1] == "$":
                    doc_count += 1
                    Q.append((i, w - 1))
                elif ord("a") <= ord(rows[-1]) < ord("z"):
                    Q.append((i, w - 1))
                    keys.append(rows[-1])
                else:
                    doors.append((rows[-1].lower(), i, w - 1))
                visited[i][0], visited[i][-1] = True, True
    temp = list(input().strip())
    if temp[0] != "0":
        keys = list(set(keys + temp))
    
    #2. Q를 조사
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for key in keys:
        indexes = []
        for i in range(len(doors)):
            if doors[i][0] == key:
                Q.append((doors[i][1], doors[i][2]))
                indexes.append(i)
        indexes.sort(reverse=True)
        for index in indexes:
            del doors[index]
    
    while Q:        
        now_x, now_y = Q.popleft()
        visited[now_x][now_y] = True
        
        for i in range(4):
            adj_x = now_x + dx[i]
            adj_y = now_y + dy[i]
            if 0 <= adj_x < h and 0 <= adj_y < w:
                if not visited[adj_x][adj_y] and maps[adj_x][adj_y] != "*":
                    current = maps[adj_x][adj_y]
                    if current == ".":
                        Q.append((adj_x, adj_y))
                    elif current == "$":
                        Q.append((adj_x, adj_y))
                        doc_count += 1
                    elif ord("a") <= ord(current) <= ord("z"):
                        Q.append((adj_x, adj_y))
                        keys.append(current)
                        keys = list(set(keys))
                        for key in keys:
                            indexes = []
                            for i in range(len(doors)):
                                if doors[i][0] == key:
                                    Q.append((doors[i][1], doors[i][2]))
                                    indexes.append(i)
                            indexes.sort(reverse=True)
                            for index in indexes:
                                del doors[index]
                        print(doors)
                        print()
                    else:
                        if current.lower() in keys:
                            Q.append((adj_x, adj_y))
                        else:    
                            doors.append((current.lower(), adj_x, adj_y))
                    visited[adj_x][adj_y] = True
        
    answers.append(doc_count)
                
for answer in answers:
    print(answer)
        
        
    