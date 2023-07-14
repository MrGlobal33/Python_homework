# from database import *
# from view import * 

# def main():
#       while True:
#             num = input_num()
#             if num == 1:
#                   info = input_info()
#                   write_info(info)
#             elif num == 2:
#                   char = input_char()
#                   find_info(char)
#             elif num == 5:
#                   print("Выход из программы...")
#                   break
            
# main()

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

from database import *
from view import * 

def main():
    while True:
        num = input_num()
        if num == 1:
            info = input_info()
            append_data(info)
        elif num == 2:
            char = input_char()
            records = find_data(char)
            display_records(records)
        elif num == 3:
            char = input_char()
            records = read_data()
            records_to_remove = find_data(char)
            for record in records_to_remove:
                records.remove(record)
            write_data(records)
        elif num == 4:
            char = input_char()
            records = read_data()
            records_to_change = find_data(char)
            display_records(records_to_change)
            index = get_index()
            new_info = input_info()
            for i, record in enumerate(records):
                if record == records_to_change[index]:
                    records[i] = new_info
            write_data(records)
        elif num == 5:
            print("Выход из программы...")
            break
            
if __name__ == "__main__":
    main()




