n = int(input())

tiles = [0] * (n + 1)
tiles[1] = 1
if n >= 2:
    tiles[2] = 2

if n >= 3:
    for i in range(3, n + 1):
        tiles[i] = (tiles[i - 1] + tiles[i - 2]) % 10007

print(tiles[n])