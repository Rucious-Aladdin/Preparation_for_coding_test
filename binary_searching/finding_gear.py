def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if (array[mid] == target):
            return True
        elif (array[mid] <= target):
            start = mid + 1
        else:
            end = mid - 1
    
    return False

N = int(input())
gear_list = sorted(list(map(int, input().split())))
M = int(input())
search_list = list(map(int, input().split()))

for s in search_list:
    if (binary_search(gear_list, s, 0, N - 1)):
        print("yes", end=" ")
    else:
        print("no", end=" ")