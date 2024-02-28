def transform_coord(coord):
    check = {1:'a', 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h"}
    check2 = {e:i for i, e in check.items()}
    print(check2)
    return check2[coord[0]], int(coord[1])

def check(coord):
    if (coord[0] <= 8) and (coord[0] >= 1):
        if (coord[1] <= 8) and (coord[1] >= 1):
            return True
    return False

coord = str(input())
coord = list(coord)
coord = transform_coord(coord)

direction_x = [+1, +2, +2, +1, -1, -2, -2, -1]
direction_y = [-2, -1, +1, +2, +2, +1, -1, -2]

count = 0
for i in range(8):
    if (check([coord[0] + direction_x[i], coord[1] + direction_y[i]])):
        count += 1
print(count)