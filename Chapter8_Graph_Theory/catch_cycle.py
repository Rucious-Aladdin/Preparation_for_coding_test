from find_path_compression import find_parent_pc
from union_find import union_parent

if __name__ == "__main__":
    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    for i in range(1, v + 1):
        parent[i] = i
        
    cycle = False

    for i in range(e):
        a, b = map(int, input().split())
        p1 = find_parent_pc(parent, a)
        p2 = find_parent_pc(parent, b)
        print("p1, p2: " + str(p1) + " " + str(p2))
        if p1 == p2:
            cycle = True
            break
        else:
            union_parent(parent, a, b)

    if cycle:
        print("사이클이 발생했습니다.")
    else:
        print("사이클이 발생하지 않았습니다.")