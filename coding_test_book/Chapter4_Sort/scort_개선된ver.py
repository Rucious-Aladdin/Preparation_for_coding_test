n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array = sorted(array, key = lambda x : x[1]) # 람다식을 이용해서 어떤것을 기준으로 정렬할지 지정가능함.
# 여기서는 리스트의 각원소의 두번째 요소를 기준으로 오름차순으로 정렬한 것임.

for student in array:
    print(student[0], end = " ")