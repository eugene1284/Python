'''
Напишите программу, которая по заданному номеру четверти показывает диапазон 
возможных координат точек в этой четверти (x и y).
'''
n = float(input('номер четверти: '))

if n==1:
    print('диапазон координат х > 0, y > 0')
elif n==2:
    print('диапазон координат х < 0, y > 0')
elif n==3:
    print('диапазон координат х < 0, y < 0')
elif n==4:
    print('диапазон координат х > 0, y < 0')
else:
    print('такой четверти в координатной плоскости 0ХУ не существует')