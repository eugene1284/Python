"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
6782 -> 23
0,56 -> 11
"""
"""
def sum_of_number(number: any):
   sum = 0
   num = str(number).replace(".", "")
   num = str(number).replace("-", "")
   for index in num:
      sum += int(index)
   return sum

number = input("Введите число: ")
print('Вы ввели: ', number, '. \nCумма цифр введённого вами числа: ', sum_of_number(number))
"""

#2 вариант
stroka = input()
summa = 0
for i in stroka:
   if i != '.':
      summa = summa + int(i)
print('summa',summa)


#3 вариант
stroka = input()
summa = 0
for i in stroka:
   if i.isdigit():
      summa = summa + int(i)
print('summa',summa)

#4 вариант
number = float(input('Введите вещественное число: '))
count = 0
while type(number) == float:
   number *= 10
   print(number)
   count += 1
   if count == 10:
      break
print(number)
