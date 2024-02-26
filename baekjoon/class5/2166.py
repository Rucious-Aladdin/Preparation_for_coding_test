import sys
input = sys.stdin.readline
N = int(input())
coords = []

for i in range(N):
    x, y = map(int, input().split())
    coords.append((x, y))

def triangle(pos1, pos2, pos3):
    x1, y1 = pos1
    x2, y2 = pos2
    x3, y3 = pos3
    return 0.5 * (x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3)

total_area = 0
for i in range(0, len(coords) - 2):
    pos1 = coords[0]
    pos2 = coords[i + 1]
    pos3 = coords[i + 2]
    total_area += triangle(pos1, pos2, pos3)
print(round(abs(total_area), 1))