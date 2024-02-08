M, N = map(int, input().split())

nums = [1] * (N + 1)
nums[0] = 0
nums[1] = 0

for i in range(2, N + 1):
    if nums[i] == 1:
        for j in range(1, (N // i) + 1):
            if j != 1:
                nums[i * j] = 0
            
for i in range(M, N + 1):
    if nums[i] == 1:
        print(i)