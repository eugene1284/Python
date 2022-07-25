"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

#import random as rd
#print(rd.randint(1,100))

from random import randint as rdi

k = int(input("enter the degree of the polynomial: "))

if k <= 0:
    print("please, enter natural number")
    exit()

polynomial = ''
for i in range(k, 0, -1):
    random_number = rdi(-100, 100)
    if random_number == 0:
        polynomial += ''
    elif random_number < 0:
        polynomial += str(f'{random_number}x^{i}')
    else:
        polynomial += str(f'+{random_number}x^{i}')

random_number = rdi(-100, 100)

if random_number > 0:
    polynomial += str(f'+{random_number} = 0')
elif random_number < 0:
    polynomial += str(f'{random_number} = 0')
else:
    polynomial += str(f'= 0')

print(polynomial)