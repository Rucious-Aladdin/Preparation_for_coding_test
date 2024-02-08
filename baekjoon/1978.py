N = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    if num == 1:
        continue
    elif num == 2:
        count += 1
    else:
        divide = 0
        for i in range(1, int(num ** 0.5 + 1)):
            if (num % i == 0):
                divide += 1
        if divide == 1:
            count += 1
        else:
            continue
print(count)