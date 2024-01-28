array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #파이썬만 가능. 대부분은..temp만들어야하는거.. 알지?
    
print(array)


"""" swap(c example.)
#include <stdio.h>

int main(){
    int a;
    int b;
    int temp;
    
    a = 3;
    b = 5;
    
    temp = a;
    
    a = b;
    b = temp;
    return 0;
}

"""