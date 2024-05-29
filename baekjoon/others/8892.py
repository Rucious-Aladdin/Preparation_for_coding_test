
from itertools import permutations

def is_valid(x):
    if len(x) == 1:
        return True
    else:
        for i in range(len(x) // 2):
            if x[i] != x[-(i + 1)]:
                return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    indexes = [i for i in range(N)]
    strings = []
    for _ in range(N):
        strings.append(input())
    
    for x in permutations(indexes, 2):
        y = [strings[x[0]], strings[x[1]]]
        if is_valid("".join(y)):
            print("".join(y))
            break
    else:
        print(0)