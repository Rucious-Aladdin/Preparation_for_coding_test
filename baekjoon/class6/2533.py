import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    graphs = [[] for i in range(N)]
    root = None
    for i in range(N - 1):
        
        src, dest = list(map(lambda x: int(x) - 1, input().split()))
        graphs[src].append((src,dest))
        graphs[dest].append((dest, src))

        if root is None:
            root = src


    Q = deque(graphs[root])
    visited = [False] * N
    levels = [0] * N
    levels_dict = defaultdict(list)
    levels_dict[0] = [(0, None)] # node 0 is root node
    max_level = 0
    while Q:
        src, dest = Q.popleft()
        visited[src] = True
        cur_level = levels[src]

        if not visited[dest]:
            dest_level = cur_level + 1
            visited[dest] = True
            levels[dest] = dest_level
            levels_dict[dest_level].append((dest, src))

            for node in graphs[dest]:
                Q.append((dest, node[1]))
            
            if dest_level >= max_level:
                max_level = dest_level

    is_early = [False] * N
    is_earlied = [False] * N
    answer = 0
    for i in range(max_level, 0, -1):
        nodes = levels_dict[i]

        for node in nodes:
            child, parent = node
            if is_early[child]:
                continue

            if (not is_early[parent]):
                is_early[parent] = True
                answer += 1

    print(answer)

