N = int(input())
nums = list(map(int, input().split()))

def search(nums, index):
    x1 = nums[index]
    start = index + 1
    end = len(nums) - 1
    mid = (start + end) // 2
    value_mid = x1 + nums[mid]
    
    while abs(end - start) > 1:
        mid = (start + end) // 2
        value_mid = x1 + nums[mid]
        if value_mid == 0:
            return 0, x1, nums[mid]
        elif value_mid > 0:
            end = mid
        elif value_mid < 0:
            start = mid
    
    answers = []
    answers.append((abs(x1 + nums[start]), x1, nums[start]))
    answers.append((abs(x1 + nums[mid]), x1, nums[mid]))
    answers.append((abs(x1 + nums[end]), x1, nums[end]))
    answers.sort(key = lambda x : x[0])
    return answers[0] 
        

min_val = int(1e12)
min_l1, min_l2 = 0, 0
for i in range(N - 1):
    value, l1, l2 = search(nums, i)
    if value <= min_val:
        min_l1, min_l2 = l1, l2
        min_val = value

print(int(min_l1), int(min_l2))