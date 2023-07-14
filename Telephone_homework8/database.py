
# def write_info(info):
#       with open("data.txt", "a") as file:
#             file.write(info)

# def find_info(char):
#       with open("data.txt","r") as file:
#             list = file.readlines()
#             count = 0 
#             for line in list:
#                   if char in line:
#                     count += 1
#                   print(f"{count})) {line.strip()}") 

def read_data():
          with open("data.txt", "r") as file:
           lines = file.readlines()
           return [line.strip().split(',') for line in lines]

def write_data(data):
    with open("data.txt", "w") as file:
        for record in data:
            file.write(','.join(record) + '\n')

def append_data(info):
          with open("data.txt", "a") as file:
           file.write(','.join(info) + '\n')


def find_data(char):
          data = read_data()
          result = [record for record in data if any(char in element for element in record)]
          if result:
           return result
          else:
           print("Пользователь не найден.")
           return []








