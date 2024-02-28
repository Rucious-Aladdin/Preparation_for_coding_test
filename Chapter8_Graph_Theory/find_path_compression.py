def find_parent_pc(parent, x):
    if parent[x] != x:
        #매우 핵심적인 부분. 재귀 함수의 반환값을 이용해 부모테이블을 갱신함.
        parent[x] = find_parent_pc(parent, parent[x])
    return parent[x]