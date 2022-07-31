"""
Создайте программу для игры в "Крестики-нолики".
"""

def check(arr):
    if (arr[0][0] == 'X' and arr[0][1] == 'X' and arr[0][2] == 'X' or
        arr[1][0] == 'X' and arr[1][1] == 'X' and arr[1][2] == 'X' or
        arr[2][0] == 'X' and arr[2][1] == 'X' and arr[2][2] == 'X' or
        arr[0][0] == 'X' and arr[1][0] == 'X' and arr[2][0] == 'X' or
        arr[0][1] == 'X' and arr[1][1] == 'X' and arr[2][1] == 'X' or
        arr[0][2] == 'X' and arr[1][2] == 'X' and arr[2][2] == 'X' or
        arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X' or
        arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X'):
        result = "X"
        return result
    elif (  arr[0][0] == '0' and arr[0][1] == '0' and arr[0][2] == '0' or
            arr[1][0] == '0' and arr[1][1] == '0' and arr[1][2] == '0' or
            arr[2][0] == '0' and arr[2][1] == '0' and arr[2][2] == '0' or
            arr[0][0] == '0' and arr[1][0] == '0' and arr[2][0] == '0' or
            arr[0][1] == '0' and arr[1][1] == '0' and arr[2][1] == '0' or
            arr[0][2] == '0' and arr[1][2] == '0' and arr[2][2] == '0' or
            arr[0][0] == '0' and arr[1][1] == '0' and arr[2][2] == '0' or
            arr[0][2] == '0' and arr[1][1] == '0' and arr[2][0] == '0'):
        result = "0"
        return result

arr = [["-","-","-"],
       ["-","-","-"],
       ["-","-","-"]]

for i in range(9):
    if i % 2 == 0:
        step = "X"
        print("Сейчас ходят Х")
    else:
        step = "0"
        print("Сейчас ходят 0")

    row = int(input("Введите номер строки: "))
    while (row < 1 or row > 3):
        print("введите число от 1 до 3")
        row = int(input("Введите номер строки: "))

    columns = int(input("Введите номер столбца: "))
    while (columns < 1 or columns > 3):
        print("введите число от 1 до 3")
        columns = int(input("Введите номер столбца: "))

    if arr[row - 1][columns - 1] == "X" or arr[row - 1][columns - 1] == "0":
        print("Эта клетка занята, ты пропускаешь ход")
    else:
        arr[row - 1][columns - 1] = step
    print(arr)
    result = check(arr)
    if result == "X":
        print("Выиграли XXX")
        break
    elif result == "0":
        print("Выиграли 000")
        break