"""
*5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""

k = int(input())
a0 = 0
a1 = 1
a2 = 2
arr = []
for i in range(k):
    arr.append(a0)
    a2 = a1 + a0
    a0 = a1
    a1 = a2
arr.append(a0)
arr1 = list()
for i in range(len(arr)):
    if i % 2 == 0:
        arr1.append(arr[i] * (-1))
    else:
        arr1.append(arr[i])
print(arr1[len(arr):1:-1] + arr)