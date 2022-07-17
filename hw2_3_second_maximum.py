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
list = [1,7,9,0,1,9,15]

max = list[0]
i = 1

while i < len(list):
    if list[i] > max:
        max = list[i]
        index_of_max = i
    i += 1

list[index_of_max] = 0
print(list)

second_max = list[0]
j = 1
while j < len(list):
    if list[j] > second_max:
        second_max = list[j]
        index_of_second_max = j
    j += 1

print(second_max)