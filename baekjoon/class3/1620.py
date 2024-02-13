import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_to_num = {}
num_to_word = {}

for i in range(N):
    name = input().strip()
    word_to_num[name] = (i + 1)
    num_to_word[i + 1] = name

answer= []
for j in range(M):
    name_num = input().strip()
    if ord("0") <= ord(name_num[0]) <= ord("9"):
        name_num = int(name_num)
        answer.append(num_to_word[name_num])
        #print(num_to_word[name_num])
    else:
        answer.append(word_to_num[name_num])
        #print(word_to_num[name_num])


for ans in answer:
    print(answer)