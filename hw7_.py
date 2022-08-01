"""
Задача:         Составить таблицы с данными по ученикам в школе.


Необходимые данные:
                    ФИО ученика
                    год рождения
                    класс
                    место в классе(ряд, парта, вариант)
                    статус по оценкам(отличник, ударник, троечник или двоечник) и другие данные, которые захочется хранить

Можно сделать минимум две таблицы: «Ученики» и «Кабинет»:
В учениках хранить данные по ученику, а в кабинете хранить — по рядам, партам, вариантам.
И связать эти таблицы между собой.
Надо пояснить, что в этом кабинете могут быть другие ученики(на другом уроке),
и мы можем использовать таблицу «Кабинет» для записи сведений о разных классах / уроках.
*** Далее выделить отдельно таблицу адреса и в ней отметить личные адреса учеников и адрес школы.
Показать, что в таблице адреса могут принадлежать ученикам или школе / работе родителей и так далее.
Адрес — это отдельная сущность.
***Выделить номер телефона в отдельную таблицу и добавить телефоны учеников и телефон школы.
4 *.Вместо таблицы “Ученик”, сделать таблицу “Люди” и добавить статус – ученик, учитель, родитель.
Связать её с номерами телефона, адресами, кабинетами

Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
- под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель

*Фамилия_1*

*Имя_1*

*Телефон_1*

*Описание_1*

*Фамилия_2*

*Имя_2*

*Телефон_2*

*Описание_2*

*и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***

*Фамилия_1,Имя_1,Телефон_1,Описание_1*

*Фамилия_2,Имя_2,Телефон_2,Описание_2*

*и т.д.*
** (Модульность) Логирование, Главный файл и тд****
"""