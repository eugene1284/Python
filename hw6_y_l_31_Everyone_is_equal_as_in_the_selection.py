"""Все равны, как на подбор

    Ограничение времени 1 секунда
    Ограничение памяти 64Mb
    Ввод стандартный ввод или input.txt
    Вывод стандартный вывод или output.txt

Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращает True, если это так.
Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True.
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

    Пример 1
    Ввод:
        values = [0, 2, 10, 6]
        if same_by(lambda x: x % 2, values):
        print('same')
        else: print('different')
    Вывод:
        same

    Пример 2
    Ввод:
        values - [1, 2, 3, 4]
        if same_by(lambda x: x % 2, values):
        print('same")
        else:
        print('different')
    Вывод:
        different
"""
def same_by(characteristic, objects):
    a = []
    for i in objects:
        if characteristic(i) == 0:
            a.append(True)
        else:
            a.append(False)
    y = a[0]
    b = list(filter(lambda x: x == y, a))
    if len(a) == len(b):
        return True
    else:
        return False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')