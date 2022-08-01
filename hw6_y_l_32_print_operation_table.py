"""
Вам уже приходилось писать таблицу умножения. Но на этот раз вас попросили сделать в плюс к таблице умножения ещё и таблицу сложения, а также таблицу возведения в степень.
Чтобы не копировать один и тот же код и обобщить все три функции до единой функции рисования таблиц (бинарных) арифметических операций,
напишите функцию print_operation_table(operation, num_rows=9, num_columns=9),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идёт с единицы (подумайте, почему не с нуля).

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
    Пример 1
        Ввод: print_operation_table(lambda x, y: x * y) 1
        Вывод: см картинку

    Пример 2
        Ввод: print_operation_table(lambda x, y: x * y, 5) 1
        Вывод: см картинку
"""

def print_operation_table(operation, number_rows, number_columns):
    if operation == '*':
        for i in range(1, number_rows + 1):
            for j in range(i, i * number_columns + 1, i):
                print(j, end='\t')
            print()
    if operation == '+':
        for i in range(1, number_rows + 1):
            for j in range(i, i + number_columns + 1, i):
                print(j, end='\t')
            print()
    if operation == '**':
        for i in range(1, number_rows + 1):
            for j in range(i, i ** number_columns + 1, i):
                print(j, end='\t')
            print()

operation = str(input('Enter operation: '))
number_rows = int(input('Enter count rows: '))
number_columns = int(input('Enter count columns: '))
print_operation_table(operation, number_rows, number_columns)