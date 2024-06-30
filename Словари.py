# 8.1. Пользователь
# Пользователь вводит имя, фамилия, возраст. Создайте словарь user и запишите данные пользователя в него.

# firstname = input('Введите имя: ')
# secondname = input('Введите фамилию: ')
# age = input('Введите возраст: ')
#
# user = dict(firstname=firstname, secondname=secondname, age=age)
# print(user)

# 8.2. Найти слово
# Выведите самое часто встречающееся слово в введённой строке.

# list_of_words = ['hello', 'hello', 'go', 'the']
# words = {}
#
# for word in list_of_words:
#     words[word] = words.get(word, 0) + 1
#     print(words)
#
# freq_word = max(words, key=words.get)
#
# print(freq_word)


# 8.3. Фрукты
# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате:
# название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ,
# а количество - значение

# K = int(input('Количество фруктов: '))
# fruits = {}
#
# for _ in range(K):
#     fru = input('Введите фрукт: ')
#     fru_key = input('Введите количество фруктов: ')
#     fruits[fru] = fru_key
#
# for fru, fru_key in fruits.items():
#     print(f'{fru}: {fru_key}')

# 8.4. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

# N = int(input('Введите количество друзей: '))
# friends = []
#
# for i in range(N):
#     name = input('Введите имя: ')
#     age = int(input('Ведите возраст: '))
#     r = {"name": name, "age": age}
#     friends.append(r)
# print(friends)
#
# youngest = min(friend["age"] for friend in friends)
# youngest_name = next(friend["name"] for friend in friends if friend["age"] == youngest)
# print(youngest_name)

# 8.5. Ещё немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

# N = int(input('Введите количество друзей: '))
# friends = []
#
# for i in range(N):
#     name = input('Введите имя: ')
#     age = int(input('Ведите возраст: '))
#     r = {"name": name, "age": age}
#     friends.append(r)
# print(friends)
#
#
# print(max(friends, key=lambda x: len(x["name"]))["name"])
# print(int(sum(friend["age"] for friend in friends) / len(friends)))

# 8.6. Английский словарь
# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка.
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.
# В этой задаче нужно использовать строчный метод split().

words = int(input('Введите количество слов для записи: '))
dicti = {}

for i in range(words):
    word = input('Введите английское слово: ').strip()
    transl = input('Введите слово или слова, обозначающие перевод этого слова: ')
    transl_lst = [t.strip() for t in transl.split(',')]
    dicti[word] = transl_lst

print(dicti)
