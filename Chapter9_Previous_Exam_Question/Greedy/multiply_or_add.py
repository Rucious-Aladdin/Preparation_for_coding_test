nums = list(input())
nums = [int(num) for num in nums]
print(nums)
product = 0

for num in nums:
    if product == 0:
        product += num
    else:
        if num <= 1:
            product += num
        else:
            product *= num
        
print(product)