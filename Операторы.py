# 2.1. Одинаковая чётность
# Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую чётность".
# (ввод 0 и 1 / 2 и 10, вывод False / True)

# print(0 % 2 == 0 and 1 % 2 == 0)
# print(' ')
# print(2 % 2 == 0 and 10 % 2 == 0)

# 2.2. Одно положительное
# # Даны три целых числа: A, B, C. Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное".

# print(0 > 0 or -1 > 0 or -10 > 0)
# print()
# print(-1 > 0 or 1 > 0 or 0 > 0)

# 2.3. Последняя цифра
# Дано натуральное число. Выведите его последнюю цифру.

# a = int(input('Введите натуральное число: '))
# print()
# print(a % 10)

# 2.4. Цифры двузначного
# Дано двузначное число. Найдите сумму его цифр.

# a = int(input('Введите двухзначное число: '))
# print()
# print('Сумма двухзначных чисел =', (a % 10) + (a // 10))

# 2.5. Цифры трёхзначного
# Дано трёхзначное число. Найдите сумму его цифр.

# a = int(input('Введите трёхзначное число: '))
# print()
# print('Сумма трёхзначных чисел =', (a % 10) + ((a // 10) % 10) + (a // 100))

# 2.6. Разные цифры
# Дано трёхзначное число. Проверить истинность высказывания: "Все цифры данного числа различны".

# a = int(input('Введите трёхзначное число: '))
# one = a % 10
# two = (a // 10) % 10
# three = a // 100
# print()
# print(one != two and one != three and two != three)

# 2.7. Часы (финальный босс)
# С начала суток прошло N секунд (N - целое). Найти количество часов, минут и секунд на электронных часах.

# time = int(input('Введите время в секундах: '))
# h = time // 3600
# m = (time % 3600) // 60
# s = time % 60
# print(f'{h}:{m}:{s}')