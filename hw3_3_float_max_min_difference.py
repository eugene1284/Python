"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

def difference(list):
    num = [round(x - int(x), 2) for x in(list)]
    num = [x for x in num if type(x) == float]
    return max(num) - min(num)


list = [1.1, 1.2, 3.1, 5, 10.01]
print(list, '= >', difference(list))