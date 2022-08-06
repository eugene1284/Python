from p8_database_students_logger import input_data, print_data, put_data, delete_data


def interface():
    print('Доброго времени суток! Вы попали на специальную программу от нашей группы! Что же мы можем делать?\n'
          '1. Записать данные(в 2-ух форматах)\n'
          '2. Удалить данные\n'
          '3. Изменить данные\n'
          '4. Вывести данные\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 4:
        print('Ты дурак?! Даю тебе последний шанс')
        command = int(input("Введите номер операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()

interface()