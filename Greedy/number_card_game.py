N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

nums = []
for i in range(N):
    nums.append(min(matrix[i]))
    
print(max(nums))