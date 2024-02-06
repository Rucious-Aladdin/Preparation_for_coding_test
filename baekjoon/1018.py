N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(input()))

answers = []
for offset_x in range(0, N - 7):
    for offset_y in range(0, M - 7):
        black = 0
        white = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    if (maps[offset_x + i][offset_y + j] != "B"):
                        black += 1
                else:
                    if (maps[offset_x + i][offset_y + j] != "W"):
                        black += 1


        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    if (maps[offset_x + i][offset_y + j] != "W"):
                        white += 1
                else:
                    if (maps[offset_x + i][offset_y + j] != "B"):
                        white += 1
        answers.append(min(black, white))
        
print(min(answers))