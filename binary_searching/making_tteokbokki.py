def bi_search(length_list, target, start, end):
    mid = 0
    while (abs(start - end) != 1):
        sum = 0
        mid = (start + end) // 2
        for i in range(len(length_list)):
            if length_list[i] > mid:
                sum += (length_list[i] - mid)
            else:
                break
        if (sum < target):
            end = mid - 1
        else:
            start = mid + 1
    
    s_sum = 0
    for i in range(len(length_list)):
        if length_list[i] > start:
            s_sum += (length_list[i] - start)
        else:
            break
    e_sum = 0
    for i in range(len(length_list)):
        if length_list[i] > end:
            e_sum += (length_list[i] - end)
        else:
            break
    
    X = sorted([(start, s_sum), (end, e_sum)], key = lambda x : x[1])
    if (X[1][1] >= target):
        return X[1][0]
    else:
        return X[0][0]
    

N, M = map(int, input().split())
length_list = sorted(list(map(int, input().split())), reverse=True)
print(length_list)

max_l = length_list[0]
min_l = 0

H = bi_search(length_list, M, min_l, max_l)
print(H)