N = int(input())
nums = list(map(int, input().split()))
values = [1] * N
for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            values[i] = max(values[i], values[j] + 1)
            
print(max(values))