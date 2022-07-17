"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
6782 -> 23
0,56 -> 11
"""
def sum_of_number(number: any):
   sum = 0
   num = str(number).replace(".", "")
   for index in num:
      sum += int(index)
   return sum


number = input("Введите число: ")
print('Вы ввели: ',number, '. \nCумма цифр введённого вами числа: ', sum_of_number(number))