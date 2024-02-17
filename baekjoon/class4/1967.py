import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for i in range(N + 1)]
tree_info = [[0, 0] for i in range(N + 1)] #지름, 긴길이.

for i in range(N - 1):
    root, child, cost = map(int, input().split())
    tree[root].append(child)
    tree_info[child][1] = cost

def findsecond(arr):
    second = first = -1

    for n in arr:
        if n > first:
            second = first
            first = n
        elif second < n < first:
            second = n
    return int(first), int(second)

def search_tree(tree, tree_info, root):
    if len(tree[root]) == 0:
        return
    elif len(tree[root]) == 1:
        next_node = tree[root][0]
        search_tree(tree, tree_info, next_node)
        tree_info[root][1] += tree_info[next_node][1]
    else:
        lengths = []
        for child in tree[root]:
            search_tree(tree, tree_info, child)
            lengths.append(tree_info[child][1])
        l1, l2 = findsecond(lengths)    
        tree_info[root][0] = l1 + l2
        tree_info[root][1] += max(lengths)
    
search_tree(tree, tree_info, 1)
print(max(max(tree_info, key=lambda x : (x[0]))[1], max(tree_info, key=lambda x : (x[0]))[0]))