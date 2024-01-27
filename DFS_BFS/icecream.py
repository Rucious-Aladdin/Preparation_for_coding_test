from collections import deque
def search(start, bowl):
    queue = deque([start])
    
    if (bowl[start[0]][start[1]] == 1):
        return bowl, 0
    else:
        bowl[start[0]][start[1]] = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while queue:
            start = queue.popleft()
            for i in range(4):
                if (start[0] + dx[i] < N) and (start[0] + dx[i] >= 0) and \
                    (start[1] + dy[i] < M) and (start[1] + dy[i] >= 0) and \
                    (bowl[start[0] + dx[i]][start[1] + dy[i]] == 0):
                    queue.append((start[0] + dx[i], start[1] + dy[i]))
                    bowl[start[0] + dx[i]][start[1] + dy[i]] = 1    
        
        return bowl, 1


N, M = map(int, input().split())
bowl = []
for i in range(N):
    temp = list(map(str, input()))
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    bowl.append(temp)

count = 0
for i in range(N):
    for j in range(M):
        bowl, temp = search((i, j), bowl)
        print(bowl, temp)
        count += temp

print(count)