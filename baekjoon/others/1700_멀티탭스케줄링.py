N, K = map(int, input().split())

seq = list(map(int, input().split()))
plug_count = 0
plug_dict = {k:False for k in range(1, K+1)}
answer = 0
last_plug = seq[0]

def check(seq, idx, plug_dict):
    exist_plug = []
    for k, v in plug_dict.items():
        if v:
            exist_plug.append(k)
    exist_order = [int(1e9) for _ in range(len(exist_plug))]
    exist_dict = {x:i for i, x in enumerate(exist_plug)}
    idx2plug = {v:k for k, v in exist_dict.items()}
    
    for i in range(len(seq) - 1, idx, -1):
        if seq[i] in exist_plug:
            if exist_order[exist_dict[seq[i]]] > i:
                exist_order[exist_dict[seq[i]]] = i
    return idx2plug[exist_order.index(max(exist_order))]

def allocate(seq, idx, plug_dict, N):
    cur_plug = seq[idx]
    global plug_count
    if plug_dict[cur_plug]: # 이미 꽂혀 있는 경우
        return False, cur_plug
    elif plug_count < N: # 빈 자리가 있는 경우
        plug_count += 1
        plug_dict[cur_plug] = True
        return False, cur_plug
    elif plug_count == N: # 자리가 없어서 뽑아야 할 경우
        off_plug = check(seq, idx, plug_dict)
        plug_dict[off_plug] = False
        plug_dict[cur_plug] = True
        return True, cur_plug
    

for i in range(len(seq)):
    alloc_Flag, last_plug = allocate(seq, i, plug_dict, N)     
    exist_plug = []
    for k, v in plug_dict.items():
        if v:
            exist_plug.append(k)
    print("current device -> %d || " % seq[i], end=" ")
    print(*exist_plug)            
    if alloc_Flag:
        answer += 1
print(answer)