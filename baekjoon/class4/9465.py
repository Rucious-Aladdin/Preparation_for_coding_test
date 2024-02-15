T = int(input())
answer = []
for i in range(T):
    N = int(input())
    stikers = []
    for i in range(2):
        stikers.append(list(map(int, input().split())))
    
    for j in range(1, len(stikers[0])):
        for i in range(2):
            if j == 1:
                if i == 0:
                    stikers[i][j] += max(0, stikers[1][j - 1])
                else:
                    stikers[i][j] += max(0, stikers[0][j - 1])
            else:
                if i == 0:
                    stikers[i][j] += max(0, stikers[1][j - 1], max(stikers[0][j - 2], stikers[1][j - 2]))
                else:
                    stikers[i][j] += max(0, stikers[0][j - 1], max(stikers[0][j - 2], stikers[1][j - 2]))
    answer.append(max(stikers[0][-1], stikers[1][-1]))

for x in answer:
    print(x)