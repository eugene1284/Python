"""
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""
arr = "1 2 3 3 3 4 89 98 5 5 50"
arr = [int(i) for i in arr.split()]

li = []
for i in arr:
    if i not in li:
        li.append(i)

print(li)