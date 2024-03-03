#두선분의 교차 판정
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = y2 - y1
b = -(x2 - x1)
e = -y1 * (x2 - x1) + x1 * (y2 - y1)

c = y4 - y3
d = -(x4 - x3)
f = -y3 * (x4 - x3) + x3 * (y4 - y3)

determinant = a * d - b * c
def get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key):
    l1 = [(x1, y1), (x2, y2)]
    l2 = [(x3, y3), (x4, y4)]
    if key == "x":
        l1.sort(key=lambda x : (x[0], x[1]))
        l2.sort(key=lambda x : (x[0], x[1]))
        return l1[0][0], l1[0][1], l1[1][0], l1[1][1], l2[0][0], l2[0][1], l2[1][0], l2[1][1]
    else:
        l1.sort(key=lambda x : (x[1], x[0]))
        l2.sort(key=lambda x : (x[1], x[0]))
        return l1[0][0], l1[0][1], l1[1][0], l1[1][1], l2[0][0], l2[0][1], l2[1][0], l2[1][1]

if determinant == 0:
    # x축에 평행
    if y1 == y2:
        x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
        if (x1 <= x3 <= x2 or x1 <= x4 <= x2) and y3 == y1:
            print(1)
            exit()
        elif (x3 <= x1 <= x4 or x3 <= x2 <= x4) and y3 == y1:
            print(1)
            exit()
        else:
            print(0)
            exit()
    # y축에 평행
    elif x1 == x2:
        x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
        if (y1 <= y3 <= y2 or y1 <= y4 <= y2) and x1 == x3:
            print(1)
            exit()
        elif (y3 <= y1 <= y4 or y3 <= y2 <= y4) and x1 == x3:
            print(1)
            exit()
        else:
            print(0)
            exit()
    # 서로 평행이므로 solution을 확인해야함
    else:
        x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
        if (x1 <= x3 <= x2):
            xa = x3
        elif (x1 <= x4 <= x2):
            xa = x4
        elif (x3 <= x1 <= x4):
            xa = x1
        elif (x3 <= x2 <= x4):
            xa = x2
        else:
            print(0)
            exit()
        if  d * (e - a * xa) == b * (f - c * xa):
            print(1)
            exit()
        else:
            print(0)
            exit()
else:
    x_sol = (e * d - b * f)
    y_sol = (a * f - e * c)
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
    if determinant > 0:
        if x1 * determinant <= x_sol <= x2 * determinant and x3 * determinant <= x_sol <= x4 * determinant:
            x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
            if y1 * determinant <= y_sol <= y2 * determinant and y3 * determinant <= y_sol <= y4 * determinant:
                print(1)
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()
    elif determinant < 0:
        if x1 * determinant >= x_sol >= x2 * determinant and x3 * determinant >= x_sol >= x4 * determinant:
            x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
            if y1 * determinant >= y_sol >= y2 * determinant and y3 * determinant >= y_sol >= y4 * determinant:
                print(1)
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()