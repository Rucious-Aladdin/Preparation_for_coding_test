def get_order(prioirty, m, n):
    queue = []
    for i in range(n):
        if i == m:
            queue.append((prioirty[i], 1))
        else:
            queue.append((prioirty[i], 0))
    count = 0
    
    while True:
        cur = queue.pop(0)
        if len(queue) == 0:
            count += 1
            break
        elif max(queue, key=lambda x : x[0])[0] > cur[0]:
            queue.append(cur)
        else:
            count += 1
            if cur[1] == 1:
                break
    return count

T = int(input())
N = []
M = []
priorities = []

for i in range(T):
    n, m = map(int, input().split())
    N.append(n)
    M.append(m)
    priorities.append(list(map(int, input().split())))

for i in range(T):
    order = get_order(priorities[i], M[i], N[i])
    print(order)