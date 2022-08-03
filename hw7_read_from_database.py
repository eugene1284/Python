database = {}
db = {'classroom': 1, 'students': 2}

def read_from_database(file_number):
    with open(f'hw7_{file_number}.txt', 'r', encoding='utf-8') as file:
        data = [i.split('\n')[0] for i in file.readlines()]
        print(data)
        database[file_number] = []
        for i in data:
            database[file_number].append(tuple(i.split(';')))
        file.close()