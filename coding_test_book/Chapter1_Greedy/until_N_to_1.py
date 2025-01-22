import time

N, K = map(int, input().split())

count = 0
while(N > K):
    if (N % K == 0):
        N = N // K
        count += 1
    else:
        rest = N % K
        N = N - rest
        count += rest
    print(N)
    time.sleep(0.7)
# 빼야할 횟수를 계산해서 한번에 빼주는 것이 가능함(시간단축)

if (N % K == 0):
    count += 1
else:
    count += (N - 1)
    
print(count)