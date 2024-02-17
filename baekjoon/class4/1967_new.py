import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for i in range(N - 1):
    root, child, cost = map(int, input().split())
    tree[root].append((child, cost))
    tree[child].append((root, cost))  # 양방향으로 연결된 트리입니다.

# 각 노드까지의 가장 긴 경로의 길이를 저장합니다.
tree_info = [0] * (N + 1)

def dfs(node, parent):
    max_length = 0
    for child, cost in tree[node]:
        if child != parent:
            length = dfs(child, node) + cost
            max_length = max(max_length, length)
    tree_info[node] = max_length
    return max_length

# 임의의 노드에서 가장 긴 경로를 찾습니다.
root_node = 1
dfs(root_node, -1)

# 트리의 지름을 계산합니다.
diameter = max(tree_info)
print(diameter)
