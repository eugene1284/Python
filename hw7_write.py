import hw7_logger

database = {}
db = {'classroom': 1, 'students': 2}

def write_in_database(file_number):
    with open(f'hw7_{file_number}.txt', 'a', encoding='utf-8') as file:
        user_input = input("введите данные для записи: ")
        file.write("\n" + str(user_input))
        file.close()
        log_from_write = "user added in file " + str(file_number) + ": '" + str(user_input) + "'"
        hw7_logger.log(log_from_write)