# 6.1. Создайте список из 10 чётных чисел и выведите его с помощью цикла for

# num = list()
#
# for i in range(2, 100):
#     if len(num) > 9:
#         break
#     else:
#         if i % 2 == 0:
#             num.append(i)
#
# print(num)

# 6.2. Создайте список из 5 элементов. Сделайте срез от второго индекса до четвёртого

# num = list(range(1, 6))
# print(num)
# cut = num[1:4]
# print(cut)

# 6.3. Создайте пустой список и добавьте в него 10 случайных чисел и выведите их.
# В данной задаче нужно использовать функцию randint.

# from random import randint
#
# num = list()
#
# for i in range(0, 10):
#     n = randint(1, 100)
#     num.append(n)
#
# print(num)

# Можно и такой способ использовать:
# while True:
#     if len(num) > 9:
#         break
#     else:
#         n = randint(1, 100)
#         num.append(n)

# 6.4. Удалите все элементы из списка, созданного в задании 3

# from random import randint
#
# num = list()
#
# for i in range(0, 10):
#     n = randint(1, 100)
#     num.append(n)
#
# num.sort()
# print(num)
#
# while len(num) > 0:
#     num.pop(0)
#
# print(num)

# Можно и такой способ использовать:
# num.clear()
# print(num)

# 6.5. Создайте список из введённой пользователем строки и удалите из него символы 'a', 'e', 'o'

# word = list(input('Введите слово или несколько слов: '))
# print(word)
# i = 0
#
# while i < len(word):
#     if word[i] == 'а' or word[i] == 'е' or word[i] == 'о':
#         word.pop(i)
#     else:
#         i += 1
#
# print(word)

# 6.6. Даны два списка, удалите все элементы первого списка из второго

# a = [1, 3, 4, 5]
# b = [4, 5, 6, 7]
#
# b = [i for i in b if i not in a]
#
# print(b)

# 6.7. Создайте список из случайных чисел и найдите наибольший элемент в нем.

# import random
#
# a = [random.randint(1, 100) for i in range(10)]
# print(a)
#
# max_num = max(a)
# print(max_num)

# 6.8. Найдите наименьший элемент в списке из задания 7

# import random
#
# a = [random.randint(1, 100) for i in range(10)]
# print(a)
#
# min_num = min(a)
# print(min_num)

# 6.9. Найдите сумму элементов списка из задания 7

# import random
#
# a = [random.randint(1, 100) for i in range(10)]
# print(a)
#
# total = 0
# for i in a:
#     total += i
# print(total)

# 6.10. Найдите среднее арифметическое элементов списка из задания 7

# import random
#
# a = [random.randint(1, 100) for i in range(10)]
# print(a)
#
# print(sum(a) / len(a))

# import random
#
# # Создаем список из 10 случайных чисел
# random_list = [random.randint(1, 100) for _ in range(10)]
# print("Список случайных чисел:", random_list)
#
# # Инициализируем переменную для хранения индекса последнего локального максимума
# last_local_max_index = -1
#
# # Итерируемся по списку, начиная с первого элемента и до предпоследнего
# for i in range(1, len(random_list) - 1):
#     # Проверяем, является ли текущий элемент локальным максимумом
#     if random_list[i] > random_list[i - 1] and random_list[i] > random_list[i + 1]:
#         last_local_max_index = i
#
# # Если список не пустой, то выводим индекс последнего локального максимума
# if last_local_max_index != -1:
#     print("Номер последнего локального максимума:", last_local_max_index)
# else:
#     print("В списке нет локальных максимумов")

# 6.11. Создайте список из случайных чисел. Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

# import random
#
# num = [random.randint(1, 101) for _ in range(10)]
# print(num)
#
# local = None
# for i in range(1, len(num) - 1):
#     if num[i - 1] < num[i] > num[i + 1]:
#         local = i
#
# if local is not None:
#     print(local)
# else:
#     print('GG')

# 6.12. Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

# import random
#
# num = [random.randint(1, 101) for _ in range(10)]
# print(num)
#
# counts = []
#
# for i in num:
#     counts.append(num.count(i))
#
# print(max(counts))

# 6.13. Создайте список из случайных чисел. Найдите второй максимум.

# import random
#
# num = [random.randint(1, 100) for _ in range(10)]
# print(num)
#
# print(max(num))
#
# num.remove(max(num))
# print(max(num))

# 6.14. Создайте список из случайных чисел. Найдите количество различных элементов в нем.

# import random
#
# random_list = [random.randint(1, 100) for _ in range(10)]
# print(random_list)
#
# unique_elements = len(set(random_list))
# print(unique_elements)