def transform(unit, num):
    if num % unit == 0:
        return unit
    elif num > unit:
        return num % unit
    else:
        return num

TC = int(input())
for i in range(TC):
    M, N, x, y = map(int, input().split())
    if M > N:
        M, N = N, M
        x, y = y, x
    
    if M == N:
        if x == y:
            print(x)
        else:
            print(-1)
    else:
        total_count = y
        first_x = transform(M, y)
        cal_x = first_x
        while cal_x != x:
            cal_x = transform(M, cal_x + (N - M))
            total_count += N
            if first_x == cal_x:
                total_count = -1
                break
        print(total_count)