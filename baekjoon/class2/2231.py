N = int(input())
nums = [1e9 for i in range(N + 1)]

for i in range(1, N + 1):
    sum = 0
    xs = list(str(i))
    for x in xs:
        sum += int(x)
    if (i + sum) <= N:
        if nums[i + sum]> i:
            nums[i + sum] = i

if nums[i] == 1e9:
    print(0)
else:
    print(nums[i])