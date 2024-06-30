# 7.1.Площадь круга
# Напишите функцию, которая получает в качестве аргумента радиус круга и находит его площадь

# def circle(a):
#     return (a * a) * 3.14
#
#
# r = int(input('Введите число для нахождения радиуса: '))
# b = circle(r)
#
# print(b)

# 7.2. На три
# Напишите функцию, которая возвращает True, если число делится на 3, и False, если - нет.


# def truth(a):
#     return a % 3 == 0
#
#
# b = int(input('Введите число: '))
# num = truth(b)
#
# print(num)

# 7.3. Максимум в списке
# Напишите функцию, которая возвращает максимальный элемент из переданного в неё списка.

# import random
#
#
# def maxlist(a):
#     return max(a)
#
#
# b = [random.randint(0, 100) for _ in range(10)]
# print(b)
# b = maxlist(b)
# print(b)

# 7.4. Сколько чётных
# Напишите функцию, которая возвращает количество чётных элементов в списке.

# import random
#
#
# def evencounter(a):
#     counter = 0
#     for elem in a:
#         if elem % 2 == 0:
#             counter += 1
#     return counter
#
#
# lst = [random.randint(0, 100) for _ in range(10)]
# print(lst)
#
# lst = evencounter(lst)
# print(lst)

# 7.5. Уникальные
# Напишите функцию, которая возвращает список с уникальными (неповторяющихся) элементам.

# import random
#
#
# def unique_elements(lst):
#     return list(set(lst))
#
#
# a = [random.randint(0, 100) for _ in range(10)]
# print(a)
#
# b = unique_elements(a)
# print(b)
