fibos = [1] * (45)
fibos[0] = 0
for i in range(2, 45):
    fibos[i] = fibos[i - 1] + fibos[i - 2]

T = int(input())
for i in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
    else:
        print(fibos[N - 1], fibos[N])