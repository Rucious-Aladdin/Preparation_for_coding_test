N = int(input())
mins = list(map(int, input().split()))

mins.sort()
for i in range(1, N):
    mins[i] += mins[i - 1]
    
print(sum(mins))