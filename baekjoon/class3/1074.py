def get_index(offset, pos, size):
    x, y = pos
    if (size == 2):
        if x == 0 and y == 0:
            return offset
        if x == 1 and y == 0:
            return offset + 1
        if x == 0 and y == 1:
            return offset + 2
        else:
            return offset + 3
    else:
        border = size // 2
        quotient = size * size // 4
        if 0 <= x < border and 0 <= y < border:
            return get_index(offset, (x, y), border)
        elif border <= x < size and 0 <= y < border:
            offset += quotient
            return get_index(offset, (x - border, y), border)
        elif 0 <= x < border and border <= y < size:
            offset += (2 * quotient)
            return get_index(offset, (x, y - border), border)
        else:
            offset += (3 * quotient)
            return get_index(offset, (x - border, y -border), border)
    
N, c, r = map(int, input().split())
size = 2 ** (N)
print(get_index(0, (r, c), size))
    
    