import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []
probs = []
temp_num = []
for i in range(N):
    nums.append(list(map(int, input().split())))
    
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    probs.append([(x1 -1, y1 - 1), (x2 - 1, y2 - 1)])
    temp_num.append(nums[x1 - 1][y1 - 1])

for i in range(N):
    for j in range(N):
        if i != 0:
            if j == 0:
                nums[i][j] += nums[i - 1][j]
            else:
                nums[i][j] = nums[i][j] +  nums[i - 1][j] + nums[i][j - 1] - nums[i - 1][j - 1]
        else:
            if j > 0:
                nums[i][j] += nums[i][j - 1]
        
    
for i, prob in enumerate(probs):
    x1, y1 = prob[0]
    x2, y2 = prob[1]
    if x1 == 0 and y1 == 0:
        print(nums[x2][y2])
    elif x1 == 0 and y1 != 0:
        print(nums[x2][y2] - nums[x2][y1 -1])
    elif x1 != 0 and y1 == 0:
        print(nums[x2][y2] - nums[x1 - 1][y2])
    else:
        print(nums[x2][y2] - nums[x1 -1][y2] - nums[x2][y1 - 1] + nums[x1 - 1][y1 - 1])
            