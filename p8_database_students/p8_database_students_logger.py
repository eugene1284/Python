from p8_database_students_data_create import name_data, surname_data, phone_data, address_data, status_data, average_mark_data,class_name_data,day_data,lesson_number_data,lesson_name_data,teacher_data,classroom_data,class_name_lessons_data


def input_data():
    user_number_table = int(input("С какой табличкой вы хотите работать?\n\n"
                                  "1. Список Людей\n"
                                  "2. Расписание\n\n"
                                  "Выберите номер варианта: "))
    if (user_number_table == 1):
        variant = int(input("В каком формате Вы хотите записать данные?\n\n"
                        "1 Вариант:\n\n"
                        "Иванов\n"
                        "Иван\n"
                        "+79991111213\n"
                        "г. Москва ул. 1-я Синичкина д3к1\n\n"
                        "Ученик\n\n"
                        "2 Вариант:\n\n"
                        "Иванов;Иван;+79991111213;г. Москва ул. 1-я Синичкина д3к1;Ученик\n\n"
                        "Выберите номер варианта: "))
        while variant != 1 and variant != 2:
            print('Ты дурак?! Даю тебе последний шанс')
            variant = int(input("Введите номер варианта: "))
        if variant == 1:
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            status = status_data()
            average_mark = average_mark_data()
            with open('p8_database_students_data_people_first_variant.csv', 'a', encoding='utf-8') as file1:
                file1.write(f'{name}\n{surname}\n{phone}\n{address}\n{status}\n{average_mark}\n\n')
        else:
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            status = status_data()
            average_mark = average_mark_data()
            with open('p8_database_students_data_people_second_variant.csv', 'a', encoding='utf-8') as file1:
                file1.write(f'{name};{surname};{phone};{address};{status};{average_mark}\n\n')

    if user_number_table == 2:
        day = day_data()
        lesson_number = lesson_number_data()
        lesson_name = lesson_name_data()
        teacher = teacher_data()
        classroom = classroom_data()
        class_name = class_name_lessons_data()
        with open('p8_database_students_lessons.csv', 'a', encoding='utf-8') as file2:
            file2.write(f'{day};{lesson_number};{lesson_name};{teacher};{classroom};{class_name}\n\n')






def print_data():
    user_number_table = int(input("С какой табличкой вы хотите работать?\n\n"
                                  "1. Список Людей первый формат\n"
                                  "2. Список Людей второй формат\n"
                                  "3. Расписание\n\n"
                                  "Выберите номер варианта: "))
    while user_number_table != 1 and user_number_table != 2 and user_number_table != 3:
        print('Ты дурак?! Даю тебе последний шанс')
        user_number_table = int(input('Введите номер файла: '))

    if user_number_table == 1:
        print('Вывожу данные для Вас 1.Список Людей первый формат\n')
        with open('p8_database_students_data_people_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            data_middle = ''
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first = data_first_version_second
            print(''.join(data_first))
            return data_first

    if user_number_table == 2:
        print('Вывожу данные для Вас 2.Список Людей второй формат\n')
        with open('p8_database_students_data_people_second_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            data_middle = ''
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first = data_first_version_second
            print(''.join(data_first))
            return data_first

    if user_number_table == 3:
        print('Вывожу данные для Вас 3.Расписание\n')
        with open('p8_database_students_lessons.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            data_middle = ''
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first = data_first_version_second
            print(''.join(data_first))
            return data_first


def put_data():
    print("1. data_people_first_variant"
          "2. data_people_second_variant"
          "3. lessons")
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second, data_thirst = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2 and number_file != 3:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        print(f'Изменить данную запись\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_first[number_journal + 1:]
        with open('p8_database_students_data_people_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    elif number_file == 2:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal + 1:]
        with open('p8_database_students_data_people_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Изменить данную запись\n{data_thirst[number_journal]}')
        day = day_data()
        lesson_number = lesson_number_data()
        lesson_name = lesson_name_data()
        teacher = teacher_data()
        classroom = classroom_data()
        class_name = class_name_lessons_data()
        data_thirst = data_thirst[:number_journal] + [f'{day};{lesson_number};{lesson_name};{teacher};{classroom};{class_name}\n'] + \
                      data_thirst[number_journal + 1:]
        with open('p8_database_students_data_people_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_thirst))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные


def print_data_for_delete(number_file):
    if number_file == 1:
        print('Вывожу данные для Вас 1.Список Людей первый формат\n')
        with open('p8_database_students_data_people_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            data_middle = ''
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first = data_first_version_second
            print(''.join(data_first))
            return data_first

    if number_file == 2:
        print('Вывожу данные для Вас 2.Список Людей второй формат\n')
        with open('p8_database_students_data_people_second_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            data_middle = ''
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first = data_first_version_second
            print(''.join(data_first))
            return data_first

    if number_file == 3:
        print('Вывожу данные для Вас 3.Расписание\n')
        with open('p8_database_students_lessons.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            data_middle = ''
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first = data_first_version_second
            print(''.join(data_first))
            return data_first

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    number_file = int(input('Введите номер файла: '))
    while number_file != 1 and number_file != 2 and number_file != 3:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))
    data_first = print_data_for_delete(number_file)



    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('p8_database_students_data_people_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    elif number_file == 2:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('p8_database_students_data_people_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('p8_database_students_data_people_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные