import datetime

def log(string):
    with open('hw7_log.txt', 'a', encoding='utf-8') as file:
        file.write("\n" + str(datetime.datetime.now()) + " " + string)
        file.close()
