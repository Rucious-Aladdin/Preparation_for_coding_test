N = int(input())
t = [0] * (N)
if N==1:
    print(1)
    exit()
t[0],t[1] = 1,3
for i in range(2, N):
    t[i] = (t[i - 1] + 2*t[i - 2]) % 10007
print(t[N-1])