
def lower_bound(nums, tgt):
    start, end = 0, len(nums) - 1
    mid = (start + end) // 2

    while start < end:
        mid = (start + end) // 2
        if nums[mid] < tgt:
            """
            tgt이 중앙값보다 크면 [start, mid] 까지는 탐색할 필요가 없는 범위가 된다.
            우리가 찾는 것은, tgt "이상"의 값이 발생하는 최초의 지점을 찾기를 원하기 때문이다.
            따라서 mid보다 한칸 큰 곳을 start로 삼아야 한다.
            """
            start = mid + 1
        else:
            """
            tgt이 중앙값보다 작거나 같으면 [mid + 1, end] 까지는 찾을 필요가 없는 지점이 되므로,
            (이 경우 같은 경우가 포함되어 있기 때문에 mid가 답이되는 경우가 있을 수도 있으므로
            보수적으로 범위를 잡아야 한다.)
            따라서 end를 mid로 잡아주면 된다.
            """
            end = mid
    """
    이분 탐색은 머리로 생각하면 까다로운 경우가 많다.
    case 나누기 -> 제외될 범위 생각 -> index 지정 순으로 생각하면 헷갈릴 일을 줄일 수 있다.ㄴ
    """
    return end

if __name__ == "__main__":
    import bisect

    N = int(input())
    nums = list(map(int, input().split()))
    LIS = [0]
    
    for num in nums:
        if LIS[-1] < num:
            LIS.append(num)
        else:
            idx = lower_bound(LIS, num)
            idx2 = bisect.bisect()
            print(idx, idx2)
            LIS[idx] = num
    
    print(len(LIS) - 1)