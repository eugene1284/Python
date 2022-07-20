"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
number_10 = int(input('Введите число: '))

bit = number_10 % 2
number_bin = bit
number_10 = number_10 // 2
i = 1

while (number_10 > 0):
    bit = number_10 % 2
    number_10 = number_10 // 2
    number_bin += bit * (10)**i
    i += 1

print("Двоичная форма записи введённого вами числа: ", number_bin)