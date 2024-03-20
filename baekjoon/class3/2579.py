N = int(input())
scores = []


for i in range(N):
    scores.append(int(input()))


if N <= 2:
    print(sum(scores))
    exit()

dp_table=[[0] * N for i in range(2)]

dp_table[0][0] = scores[0]
dp_table[0][1] = scores[1]

for i in range(1, N):
    if i >= 2: # 두칸 올라가는 경우
        dp_table[0][i] = max(dp_table[0][i - 2], dp_table[1][i - 2]) + scores[i]
    
    #한칸 올라가는 경우
    dp_table[1][i] = dp_table[0][i - 1] + scores[i]

for l in dp_table:
    print(l)

print(max(dp_table[0][-1], dp_table[1][-1]))