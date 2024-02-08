import sys
input = sys.stdin.readline
N = int(input())

age_names = []
for i in range(N):
    age, name = input().split()
    age_names.append((int(age), name, i))
age_names.sort(key=lambda x : (x[0], x[2]))

for age, name, i in age_names:
    print(str(age), name)