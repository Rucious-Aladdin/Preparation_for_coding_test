N = int(input())


pos = [0 for i in range(N)]
count = 0

def check(pos, order):
    for i in range(order):
        if pos[order] == pos[i] or abs(pos[order] - pos[i]) == abs(order - i):
            return False
    return True

def nqueen(order):
    global count
    if order == N:
        count += 1
        return
    else:
        for i in range(N):
            pos[order] = i
            if check(pos, order):
                nqueen(order + 1)
        #pos[order] = 0

nqueen(0)
print(count)
    