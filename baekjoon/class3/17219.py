import sys
input = sys.stdin.readline

N, M = map(int, input().split())

password_dict = {}

for i in range(N):
    site, password = input().split()
    password_dict[site] = password

for j in range(M):
    print(password_dict[input().strip()])    