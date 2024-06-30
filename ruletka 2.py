import random

print('Хочешь сыграть в рулетку?')
sign = input('Твой ответ (да/нет): ')
rounds = 4
lifes = 2
dealers_lifes = 2

if sign == 'нет' or sign == 'Нет':
    print('Приходи, когда захочешь поиграть')
elif sign == 'да' or sign == 'Да':
    print('Тогда сейчас начнём!')
    revolver = [4, 4, 3, 3]
    random.shuffle(revolver)
    print(revolver)
    for i in range(rounds):
        print(f'У тебя столько жизней: {lifes}')
        print(f'у меня столько жизней: {dealers_lifes}')
        print('Выстрелишь в себя или в меня? Если в себя и будет холостой, то я пропускаю ход.')
        choice = input('Твой ответ (в себя / в тебя): ')
        if lifes == 0 or dealers_lifes == 0:
            break
        if choice == 'в себя' and (revolver[0] / 2) == 0:
            lifes -= 1
            revolver.pop(0)
            print(revolver)
            print(f'Не повезло. У тебя осталась {lifes} жизнь!')
    if lifes == 0:
        print('Ты проиграл. Повезёт в следующий раз.')
    elif dealers_lifes == 0:
        print('Ты выиграл. Поздравляю!')
else:
    print('Ошибка: нужно ввести только либо слово "да", либо слово "нет"')
