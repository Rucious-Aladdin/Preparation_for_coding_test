N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0
for coin in coins:
    quotient = K // coin
    if quotient == 0:
        continue
    else:
        K -= (quotient * coin)
        count += quotient
    
    if K == 0:
        print(count)
        exit()