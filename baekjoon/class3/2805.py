N, M = map(int, input().split())
trees = list(map(int, input().split()))

def get_tree_length(trees, H):
    total_meter = 0
    for tree in trees:
        if tree > H:
            total_meter += (tree - H)
    return total_meter

start, end = 0, max(trees)
result = 0
while start <= end:
    mid = (start + end) // 2    
    cur_length = get_tree_length(trees, mid)
    
    if cur_length < M:
        end = mid - 1
    elif cur_length > M:
        result = mid
        start = mid + 1
    else:
       print(mid)
       exit()
print(result)