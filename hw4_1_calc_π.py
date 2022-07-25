"""
Вычислить число c заданной точностью d

Пример:
- при d = 3, π = 3.141
"""

d = int(input("Сколько знаков после запятой? "))

#π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - ..

k = 1
s = 0
for i in range(1000000):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
    k += 2

n = 10 ** d
res = int(s * n) / n

print("number_pi: ", s)
print("number_pi: ", res)