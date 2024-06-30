# 5.1. Чётные от A до B
# Пользователь вводит числа A и B (A > B). Выведите чётные числа от A до B включительно

# A = int(input('Введите бОльшее число: '))
# B = int(input('Введите меньшее число: '))
#
# while A >= B:
#     if A == 0:
#         break
#     elif A % 2 == 0:
#         print(A, end=' ')
#     A -= 1

# 5.2. От A до B на три
# Пользователь вводит числа A и B (A < B, A меньше B). Выведите числа от A до B включительно, которые делятся на три.

# A = int(input('Введите меньшее число: '))
# B = int(input('Введите бОльшее число: '))
#
# while A <= B:
#     if A > B:
#         break
#     elif A % 3 == 0:
#         print(A, end=' ')
#     A += 1

# 5.3. Сумма чисел
# Пользователь вводит числа до тех пор, пока не введёт 0. Выведите сумму введённых чисел (0 считать не нужно).

# n = int(input('Введите число: '))
# coun = 0 + n
# print('Если хотите завершить программу, то введите 0')
#
# while n:
#     n = int(input('Введите число: '))
#     coun = coun + n
#
# print(f'Сумма введённых Вами чисел равна {coun}')

# 5.4. Максимум
# # Пользователь вводит числа до тех пор, пока не введёт 0. Выведите максимальное введённое число (0 считать не нужно).

# n = int(input('Введите число (завершить программу: 0): '))
# max_n = n
#
# while True:
#     num = int(input('Введите число: '))
#     if num == 0:
#         break
#     if num > max_n:
#         max_n = num
#
# print(f'Максимальное число равно {max_n}')

# 5.5. Минимум
# Пользователь вводит числа до тех пор, пока не введёт 0. Выведите минимальное введённое число (0 считать не нужно).

# n = int(input('Введите число (завершить программу: 0): '))
# min_n = n
#
# while True:
#     num = int(input('Введите число: '))
#     if num == 0:
#         break
#     if num < min_n:
#         min_n = num
#
# print(f'Минимальное число равно {min_n}')

# 5.6.  Факториал
# Пользователь вводит число N. Выведите факториал число N.
# Факториал числа N - это произведение всех чисел от 1 до N включительно. Например, факториал числа 5 равен 120.

# N = int(input('Введите число: '))
# start = 1
# dif = 1
#
# while True:
#     if dif < N:
#         dif += 1
#         start = start * dif
#     else:
#         break
#
# print(f'Факториал {N} = {start}')

# 5.7. Фибоначчи (финальный босс)
# Пользователь вводит число N. Выведите N-ное по счету число Фибоначчи.
# Последовательность чисел Фибоначчи рассчитывается по такой формуле:
# F(1) = 1, F(2) = 1, F(K) = F(K-2) + F(K-1). Идея такая: каждое следующее число равно сумму двух предыдущих.
# Первые 10 чисел последовательности: 1 1 2 3 5 8 13 21 34 55 ...

# n = int(input('Введите число: '))
#
# a, b = 1, 1
# k = 2
#
# if n == 1 or n == 2:
#     print('1')
# else:
#     while k < n:
#         a, b = b, a + b
#         k += 1
#
# print(f'Число Фибоначчи под номером {n} = {b}')