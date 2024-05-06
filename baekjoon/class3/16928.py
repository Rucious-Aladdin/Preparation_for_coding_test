from collections import deque

N, M = map(int, input().split())

visited = [int(1e9)] * 101
snakes_or_ladders = [False] * 101
sorl_dict = {}
for i in range(N + M):
    s, d = map(int, input().split())
    snakes_or_ladders[s] = True
    sorl_dict[s] = d

def bfs(visited, snakes_or_ladders, sorl):
    q = deque([(1, 0)])
    visited[0] = 0
    while q:
        cur, clock= q.popleft()
        if cur == 100:
            break

        for i in range(1, 7):
            adj = cur + i
            if adj <= 100:
                if snakes_or_ladders[adj]:
                    if clock + 1 < visited[sorl[adj]]:
                        visited[sorl[adj]] = clock + 1
                        q.append((sorl[adj], clock + 1))
                else:
                    if clock + 1 < visited[adj]:
                        visited[adj] = clock + 1
                        q.append((adj, clock + 1))

bfs(visited, snakes_or_ladders, sorl_dict)
print(visited[100])