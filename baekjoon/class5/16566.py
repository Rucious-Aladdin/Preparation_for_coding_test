def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a
    
def bin_search(cards, tgt):
    start = 0
    mid = len(cards) // 2
    end = len(cards) - 1
    
    while abs(start - end) > 1:
        mid = (start + end) // 2
        if cards[mid] > tgt:
            end = mid - 1
        elif cards[mid] < tgt:
            start = mid + 1
        elif tgt == cards[mid]:
            break
    
    candies = [
        (cards[start], start), 
        (cards[mid], mid), 
        (cards[end], end)
    ]
    candies.sort(key=lambda x: (x[0], x[1]))

    for i in range(3):
        if candies[i][0] >= tgt:
            return candies[i][1]
    return mid

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    src_cards = list(map(int, input().split()))
    src_parent = [i for i in range(len(src_cards))]
    tgt_cards = list(map(int, input().split()))

    src_cards.sort()

    for tgt_card in tgt_cards:
        idx = bin_search(src_cards, tgt_card + 1)
        idx = find(src_parent, idx) # idx의 맨뒤의 disjoint set을 찾는다.
        print(src_cards[idx])
        if idx < len(src_parent) - 1: 
            union(src_parent, idx, idx+1) # idx와 idx 다음번째 숫자의 disjoint set을 합친다.
