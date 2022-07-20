"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

"""

def product(list):
    len_list = len(list)
    half_len_list = len_list / 2
    half_len_list_for_odd = int(half_len_list + 0.5)

    if len_list % 2 == 0:
            i = 0
            j = -1
            product_list = [0] * int(half_len_list)
            while i < (len(list) / 2):
                product_list[i] = list[i] * list[j]
                i += 1
                j += (-1)
            print(list, '= >', product_list)


    if len_list % 2 > 0:
            i = 0
            j = -1
            product_list = [0] * half_len_list_for_odd
            while i < (len(list) / 2):
                product_list[i] = list[i] * list[j]
                i += 1
                j += (-1)
#            product_list[i] = list[i] * list[i]
            print(list2, '= >', product_list)
    return

list = [2, 3, 5, 6]
list2 = [2, 3, 4, 5, 6]

product(list)
product(list2)

#len(list)  #4
#len(list2) #5
#len(list) % 2 == 0 #TRUE
# product_list = list[0] * list[-1]   #12
# product_list2 = list[1] * list[-2]   #15