K, N = map(int,input().split())
lans = []
for i in range(K):
    lans.append(int(input()))

def get_num_lan(length, lans):
    num_lans = 0
    for lan in lans:
        num_lans += (lan // length)
    return num_lans

max_length = max(lans)
num_lans = 0
start_length, mid_length, end_length = 1, ((1 + max_length) // 2), max_length

start_num = get_num_lan(start_length, lans)
mid_num = get_num_lan(mid_length, lans)
end_num = get_num_lan(end_length, lans)

while abs(start_length - end_length) > 1:
    if mid_num >= N: #랜선의 개수가 많으므로 길이를 더 늘려도 됨.
        start_length = mid_length
        mid_length = (start_length + end_length) // 2
        start_num = get_num_lan(start_length, lans)
        mid_num = get_num_lan(mid_length, lans)
    else: # 랜선의 개수가 모자람.
        end_length = mid_length
        mid_length = (start_length + end_length) // 2
        end_num = get_num_lan(end_length, lans)
        mid_num = get_num_lan(mid_length, lans)

x = [(start_num, start_length), (mid_num, mid_length), (end_num, end_length)]

max_length = 0
for a in x:
    if a[0] >= N:
        if a[1] > max_length:
            max_length = a[1]
print(max_length)