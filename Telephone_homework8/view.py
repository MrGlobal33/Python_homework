
# def input_num():
#       ask = int(input("1- Добавить пользователя\n2 - Наити пользователя\n5 - Выйти"))

# def input_info():
#   fio = input("Введите Фио человека - ")
#   birth = input ("Введите данных рождения")
#   tele = input ("Введите номер телефона")
#   info = f"{fio},{birth},{tele}\n"
#   return info

# def input_char():
#    char = input("Введите характеристику - ")
#    return char

def input_num():
          return int(input("1 - Добавить пользователя\n2 - Найти пользователя\n3 - Удалить пользователя\n4 - Изменить данные пользователя\n5 - Выйти\n"))

def input_info():
    fio = input("Введите ФИО человека: ")
    birth = input("Введите данные рождения: ")
    tele = input("Введите номер телефона: ")
    info = f"{fio},{birth},{tele}"
    return info.split(',')

def input_char():
    return input("Введите характеристику: ")

def display_records(records):
    for i, record in enumerate(records):
        print(f"{i + 1}) {' '.join(record)}")

def get_index():
    return int(input("Введите номер записи: ")) - 1








