N = int(input())
triangle = []
for i in range(N):
    triangle.append(list(map(int, input().split())))

for i in range(N - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] = triangle[i][j] + max(triangle[i + 1][j], triangle[i + 1][j + 1])

print(triangle[0][0])