"Реализуйте RLE-алгоритм: реализуйте модуль сжатия и восстановления данных."

string = input("Введите строку: ")
count = 1
len_string = len(string) - 1
for i in range(len_string):
    if string[i] == string[i+1]:
        count += 1
        if i == len_string - 1:
            print("В данной строке", count, " символ(а) ", "'", string[i], "'")
    else:
        print("В данной строке", count," символ(а) ","'",string[i],"'")
        a = string[i]
        count = 1


s = "2a3b"
print("\nниже демонстрируется алгоритм восстановления для заданной строки S: ",s)
count = ""
for i in range(len(s)):
    if s[i].isdigit():
        count += s[i]
    else:
        count = ""

    if s[i].isdigit() and not s[i + 1].isdigit():
        print(int(count) * s[i + 1], end="")
