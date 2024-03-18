N, M = map(int, input().split())
maps = []
for i in range(N):
    x = list(map(int, input().split()))
    maps.append(x)

def turn(block):
    row_length = len(block)
    column_length = len(block[0])
    turned_block = [[False] * row_length for i in range(column_length)]
    for i in range(column_length):
        for j in range(row_length):
            current_pixel = block[row_length - j -1][i]
            if current_pixel:
                turned_block[i][j] = current_pixel
    return turned_block

def reverse(block):
    row_length = len(block)
    column_length = len(block[0])
    reversed_block = [[False] * column_length for i in range(row_length)]
    for i in range(row_length):
        for j in range(column_length):
            current_pixel = block[i][column_length - 1 - j]
            if current_pixel:
                reversed_block[i][j] = current_pixel
    return reversed_block

def get_q(q):
    q = []
    block1 = [[True, True, True, True]]
    q.append(block1)
    q.append(turn(block1))
    block2 = [
        [True, True],
        [True, True]
    ]
    q.append(block2)
    block3 = [
        [True, True, True],
        [False, True, False]
    ]
    q.append(block3)
    for i in range(3):
        block3 = turn(block3)
        q.append(block3)
    block4 = [
        [True, False],
        [True, True],
        [False, True]
    ]
    q.append(block4)
    q.append(turn(block4))
    reversed_block4 = reverse(block4)
    q.append(reversed_block4)
    q.append(turn(reversed_block4))
    block5 = [
        [True, False],
        [True, False],
        [True, True]
    ]
    q.append(block5)
    for i in range(3):
        block5 = turn(block5)
        q.append(block5)
    reversed_block5 = reverse(block5)
    q.append(reversed_block5)
    for i in range(3):
        reversed_block5 = turn(reversed_block5)
        q.append(reversed_block5)
    return q

q = []
q = get_q(q)
max = 0
for block in q:
    row_len = len(block)
    col_len = len(block[0])
    for i in range(len(maps) - row_len + 1):
        for j in range(len(maps[0]) - col_len + 1):
            sum = 0
            for k in range(row_len):
                for l in range(col_len):
                    if block[k][l]:
                        sum += maps[i + k][j + l]
            if sum > max:
                max = sum
print(max)