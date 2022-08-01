"""
Задана последовательность натуральных чисел, завершающаяся числом 0.
Требуется определить значение второго по величине элемента в этой последовательности,
то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
Пример:
1
7
9
0
Вывод:
7
"""
def find_max(list):
    max = list[0]
    i = 1
    index_of_max = 0
    while i < len(list):
        if list[i] > max:
            max = list[i]
            index_of_max = i
        i += 1
    return max, index_of_max

list = [1,7,9,0,1,9,15]

max,index_of_max = find_max(list)
list[index_of_max] = 0
second_max,index_of_second_max = find_max(list)
print(second_max)