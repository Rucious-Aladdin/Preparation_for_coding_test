
def lower_bound(nums, tgt):
    start, end = 0, len(nums) - 1
    mid = (start + end) // 2

    while start < end:
        mid = (start + end) // 2
        if nums[mid][-1][0] < tgt:
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
    case 나누기 -> 제외될 범위 생각 -> index 지정 순으로 생각하면 헷갈릴 일을 줄일 수 있다.
    """
    return end

if __name__ == "__main__":
    # >> Input
    N = int(input())
    nums = list(map(int, input().split()))
    LIS = [[(-1e15, -1, None)]]
    
    for i, num in enumerate(nums):
        last_val, last_idx, _ = LIS[-1][-1]
        if num > last_val:
            LIS.append([(num, i, len(LIS[-1])-1)])
        else:
            # >> use Lower bound
            idx = lower_bound(LIS, num)
            if 0 <= idx -1 <= len(LIS)-1:
                LIS[idx].append((num, i, len(LIS[idx-1])-1))
    
    # >> Back Tracking
    answers = []
    top_idx = 0
    for i in range(len(LIS) - 1, 0, -1):
        answers.append(LIS[i][top_idx][0])
        _, _, top_idx = LIS[i][top_idx]
    print(len(answers))
    print(*reversed(answers))