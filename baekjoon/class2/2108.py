N = int(input())

nums = [[0, i - 4000] for i in range(8001)]

for i in range(N):
    nums[int(input()) + 4000][0] += 1

#산술 평균
sum = 0
for i in range(8001):
    sum += (nums[i][1] * nums[i][0])
print(sum / N)

#중앙값
index = N // 2 + 1
for i in range(8001):
    index -= nums[i][0]
    if index <= 0:
        print(nums[i][1])
        break
    
#최빈값
max_count = max(nums, key=lambda x : x[0])[0]
candidates = []
for i in range(8001):
    if nums[i][0] == max_count:
        candidates.append(nums[i][1])
if len(candidates) == 1:
    print(candidates[0])
else:
    candidates = sorted(candidates)
    print(candidates[1])

#범위
min_val = 1e9
max_val = -1e9
for i in range(8001):
    if nums[i][0] != 0:
        if nums[i][1] > max_val:
            max_val = nums[i][1]
        
        if nums[i][1] < min_val:
            min_val = nums[i][1]
print(max_val - min_val)