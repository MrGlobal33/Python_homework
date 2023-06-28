# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# import random

# while True:
#     n = int(input("Введите количество элементов первого множества: "))

#     set1 = set()
#     print("Введите элементы первого множества:")
#     elements1 = sorted([random.randint(1, 20) for _ in range(n)])
#     set1.update(elements1)
#     print(*elements1)

#     m = int(input("Введите количество элементов второго множества: "))

#     set2 = set()
#     print("Введите элементы второго множества:")
#     elements2 = sorted([random.randint(1, 20) for _ in range(m)])
#     set2.update(elements2)
#     print(*elements2)

#     intersection = set1.intersection(set2)

#     if intersection:
#         result = sorted(list(intersection))
#         print("Результат:", result)
#         break
#     else:
#         print("Вобоих множествах нет общих элементов. Пожалуйста, введите данные заново.")



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# import random

# def collect_berries(berries, bush_number):
#     n = len(berries)
#     bush_number -= 1 
#     harvested = berries[bush_number]  
#     left_neighbor = (bush_number - 1) % n
#     right_neighbor = (bush_number + 1) % n
#     harvested_left = berries[left_neighbor]  
#     harvested_right = berries[right_neighbor]  
#     total_harvested = harvested + harvested_left + harvested_right  
#     return harvested, left_neighbor, right_neighbor, harvested_left, harvested_right, total_harvested

# n = int(input("Введите количество кустов (минимум 3): "))
# if n < 3:
#     print("Количество кустов должно быть не менее трех.")
# else:
#     berries = [random.randint(5, 20) for _ in range(n)]
#     selected_bush = int(input("Введите номер выбранного куста: "))

#     if selected_bush < 1 or selected_bush > n:
#         print("Некорректный номер куста.")
#     else:
#         harvested, left_neighbor, right_neighbor, harvested_left, harvested_right, total_harvested = collect_berries(berries, selected_bush)

#         print("Сбор ягод с кустов:")
#         print("Куст №", selected_bush, ":", harvested, "ягод")
#         print("Левый сосед (Куст №", left_neighbor + 1, "):", harvested_left, "ягод")
#         print("Правый сосед (Куст №", right_neighbor + 1, "):", harvested_right, "ягод")
#         print("Общее количество собранных ягод:", total_harvested, "ягод")












