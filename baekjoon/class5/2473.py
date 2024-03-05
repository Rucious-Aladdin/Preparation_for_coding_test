N = int(input())
nums = list(map(int, input().split()))
nums.sort()

start = 1
end = N - 1

min_list = [0, 0, 0]
min_val = int(1e15)
zeroFlag = False

for i in range(N - 2):
    target_value = nums[i]
    start = i + 1
    end = N - 1
    
    while start < end:
        cost = nums[start] + nums[end]
        if abs(target_value + cost) < min_val:
            min_val = abs(target_value + cost)
            min_list = [nums[i], nums[start], nums[end]]
        
        if target_value + cost == 0:
            zeroFlag = True
            break
        elif target_value + cost > 0:
            end -= 1
        elif target_value + cost < 0:
            start += 1
    if zeroFlag:
        break
    
print(*min_list)