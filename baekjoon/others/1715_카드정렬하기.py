import heapq
import sys

input = sys.stdin.readline
N = int(input())
nums = []
for i in range(N):
    heapq.heappush(nums, int(input()))

total_cost = 0
while len(nums) != 1:
    card1 = heapq.heappop(nums)
    card2 = heapq.heappop(nums)
    next_card_nums = card1 + card2
    
    total_cost += next_card_nums
    heapq.heappush(nums, next_card_nums)
    print(nums)
    if len(nums) == 1:
        break 

print(total_cost)
