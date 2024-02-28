str1 = input()
str2 = input()
answer = []
dp_table = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp_table[i][j] = max(dp_table[i - 1][j - 1] + 1, dp_table[i][j - 1], dp_table[i - 1][j])
        else:
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

x, y = len(str1), len(str2)
while True:
    if str1[x - 1] == str2[y - 1]:
        answer.insert(0, str1[x - 1])
        x -= 1
        y -= 1
    else:
        if dp_table[x][y] == dp_table[x - 1][y]:
            x -= 1
        else:
            y -= 1
    
    if x == 0 or y == 0:
        break
        
print(dp_table[len(str1)][len(str2)])
print("".join(answer))