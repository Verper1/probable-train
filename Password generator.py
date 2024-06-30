# 4. Генератор паролей – простое приложение, генерирующее случайный пароль.
# Из навыков потребуется генератор случайных чисел, работа со строками, числами, вывод на экран, последовательности.

import random
import string

symbols = list(string.ascii_letters + string.digits)
random.shuffle(symbols)
nums = int(input('Введите количество символов: '))

password = ''.join(symbols[:nums])
print(password)
