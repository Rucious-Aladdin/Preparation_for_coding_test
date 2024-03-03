#두선분의 교차 판정
x1, y1, x2, y2 = map(float, input().split())
x3, y3, x4, y4 = map(float, input().split())
epsilon = 0.00000001

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

a = y2 - y1
b = -(x2 - x1)
e = -y1 * (x2 - x1) + x1 * (y2 - y1)

c = y4 - y3
d = -(x4 - x3)
f = -y3 * (x4 - x3) + x3 * (y4 - y3)

#-------a, b, c, d 가 0일 수 있는 모든 케이스에 대해서 처리---------

# a, c가 동시에 0 또는 b, d가 동시에 0 -> 둘다 y축, x축 평행인 경우
if a == 0 and c == 0:
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
    # b > 0 and d > 0 이므로 no zero division error
    if (abs(e / b - f / d) <= epsilon) and (x3 <= x1 <= x4 or x3 <= x2 <= x4):
        print(1)
        exit()
    else:
        print(0)
        exit()
elif b == 0 and d == 0:
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
    if (abs(e / a - f / c) <= epsilon) and (y3 <= y1 <= y4 or y3 <= y2 <= y4):
        print(1)
        exit()
    else:
        print(0)
        exit()

# a, c 둘중 하나가 0 -> y해를 한번에 구할수 있는 경우
if a == 0:
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
    y_sol = y1 #y1, y2가 동일
    x_sol = (f - d * y_sol) / c
    if x1 <= x_sol <= x2 and x3 <= x_sol <= x4:
        x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
        if y3 <= y_sol <= y4:
            print(1)
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()
elif c == 0:
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
    y_sol = y3
    x_sol = (e - b * y_sol) / a
    if x1 <= x_sol <= x2 and x3 <= x_sol <= x4:
        x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
        if y1 <= y_sol <= y2:
            print(1)
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()

#b, d 둘중 하나가 0 -> x해를 한번에 구할 수 있는 경우
if b == 0:
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
    x_sol = x1
    y_sol = (f - c * x_sol) / d
    if y1 <= y_sol <= y2 and y3 <= y_sol <= y4:
        x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
        if x3 <= x_sol <= x4:
            print(1)
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()
elif d == 0:
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
    x_sol = x3
    y_sol = (e - a * x_sol) / b
    if y1 <= y_sol <= y2 and y3 <= y_sol <= y4:
        x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
        if x3 <= x_sol <= x4:
            print(1)
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()

#-------a, b, c, d 모두가 0이 아닌 케이스에 대해서 처리---------
aug_matrix = [[a, b, e], 
              [c, d, f]]

for i in range(3):
    aug_matrix[0][i] *= c / a
for i in range(3):
    aug_matrix[1][i] -= aug_matrix[0][i]

alpha = aug_matrix[1][1]
beta = aug_matrix[1][2]
#for x in aug_matrix:
#    print(*x)

if abs(alpha) < epsilon and abs(beta) < epsilon: #두직선이 평행한경우
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
    if x1 <= x3 <= x2 or x1 <= x4 <= x2:
        print(1)
        exit()
    else:
        print(0)
        exit()
elif abs(alpha) < epsilon: #y가 무한 -> 해가 존재하지 않음
    print(0)
    exit()
else:
    y_sol = beta / alpha
    x_sol = (e - b * y_sol) / a
    #print(x_sol, y_sol)
    x_flag = False
    y_flag = False
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "x")
    if x1 <= x_sol <= x2 and x3 <= x_sol <= x4:
        x_flag = True
    x1, y1, x2, y2, x3, y3, x4, y4 = get_sorted_coordinates(x1, y1, x2, y2, x3, y3, x4, y4, key = "y")
    if y1 <= y_sol <= y2 and y3 <= y_sol <= y4:
        y_flag = True
    
    if x_flag and y_flag:
        print(1)
        exit(0)
    else:
        print(0)
        exit()