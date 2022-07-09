'''
Напишите программу для проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''


x = int(input('введите число x: '))
y = int(input('введите число Y: '))
z = int(input('введите число Z: '))
if not (x or y or z) == (not x) and (not y) and (not z):
    print('true')
else:
    print('false')