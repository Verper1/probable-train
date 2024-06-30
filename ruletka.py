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
        if choice == 'в себя' or choice == 'В себя' and ((revolver[0] / 2) == 0):
            lifes -= 1
            revolver.pop(0)
            print(f'Не повезло. У тебя осталась {lifes} жизнь!')
            gun = random.randint(0, 100)
            print('Теперь моя очередь.')
            if (gun >= 50) and ((revolver[0] / 2) == 0):
                dealers_lifes -= 1
                print('Я выстрелил в себя и был боевой. Было больно.')
                revolver.pop(0)
            elif (gun <= 49) and ((revolver[0] / 2) == 0):
                print('Я выстрелил в тебя и был боевой. Не повезло тебе.')
                lifes -= 1
                revolver.pop(0)
            elif gun <= 49 and ((revolver[0] / 2) > 0):
                print('Я выстрелил в тебя и был холостой. Тебе повезло.')
                revolver.pop(0)
            if gun >= 50 and ((revolver[0] / 2) > 0):
                print('Я выстрелил в себя и был холостой. Я хожу ещё раз.')
                revolver.pop(0)
                gun = random.randint(0, 100)
                if gun >= 50 and ((revolver[0] / 2) == 0):
                    dealers_lifes -= 1
                    print('Я выстрелил в себя и был боевой. Было больно.')
                    revolver.pop(0)
                elif gun <= 49 and ((revolver[0] / 2) == 0):
                    print('Я выстрелил в тебя и был боевой. Не повезло тебе.')
                    lifes -= 1
                    revolver.pop(0)
                elif (gun <= 49) and ((revolver[0] / 2) > 0):
                    print('Я выстрелил в тебя и был холостой. Тебе повезло.')
                    revolver.pop(0)
                if (gun >= 50) and ((revolver[0] / 2) > 0):
                    print('Я выстрелил в себя и был холостой. Я хожу ещё раз.')
                    revolver.pop(0)
                    gun = random.randint(0, 100)
                    if (gun >= 50) and ((revolver[0] / 2) == 0):
                        dealers_lifes -= 1
                        print('Я выстрелил в себя и был боевой. Было больно.')
                        revolver.pop(0)
                    elif (gun <= 49) and ((revolver[0] / 2) == 0):
                        print('Я выстрелил в тебя и был боевой. Не повезло тебе.')
                        lifes -= 1
                        revolver.pop(0)
                    elif (gun <= 49) and ((revolver[0] / 2) > 0):
                        print('Я выстрелил в тебя и был холостой. Тебе повезло.')
                        revolver.pop(0)
                    if (gun >= 50) and ((revolver[0] / 2) > 0):
                        print('Я выстрелил в себя и был холостой. Я хожу ещё раз.')
                        revolver.pop(0)
        elif (choice == 'в тебя' or choice == 'В тебя') and ((revolver[0] / 2) == 0):
            dealers_lifes -= 1
            revolver.pop(0)
            print(f'Знатно ты мне прописал. У меня осталась {dealers_lifes} жизнь.')
        elif (choice == 'в тебя' or choice == 'В тебя') and ((revolver[0] / 2) > 0):
            revolver.pop(0)
            print('Холостой. Было близко.')
            gun = random.randint(0, 100)
            if (gun >= 50) and ((revolver[0] / 2) == 0):
                dealers_lifes -= 1
                print('Я выстрелил в себя и был боевой. Было больно.')
                revolver.pop(0)
            elif (gun <= 49) and ((revolver[0] / 2) == 0):
                print('Я выстрелил в тебя и был боевой. Не повезло тебе.')
                lifes -= 1
                revolver.pop(0)
            elif (gun <= 49) and ((revolver[0] / 2) > 0):
                print('Я выстрелил в тебя и был холостой. Тебе повезло.')
                revolver.pop(0)
            if (gun >= 50) and ((revolver[0] / 2) > 0):
                print('Я выстрелил в себя и был холостой. Я хожу ещё раз.')
                revolver.pop(0)
                gun = random.randint(0, 100)
                if (gun >= 50) and ((revolver[0] / 2) == 0):
                    dealers_lifes -= 1
                    print('Я выстрелил в себя и был боевой. Было больно.')
                    revolver.pop(0)
                elif (gun <= 49) and ((revolver[0] / 2) == 0):
                    print('Я выстрелил в тебя и был боевой. Не повезло тебе.')
                    lifes -= 1
                    revolver.pop(0)
                elif (gun <= 49) and ((revolver[0] / 2) > 0):
                    print('Я выстрелил в тебя и был холостой. Тебе повезло.')
                    revolver.pop(0)
                if (gun >= 50) and ((revolver[0] / 2) > 0):
                    print('Я выстрелил в себя и был холостой. Я хожу ещё раз.')
                    revolver.pop(0)
                    gun = random.randint(0, 100)
                    if (gun >= 50) and ((revolver[0] / 2) == 0):
                        dealers_lifes -= 1
                        print('Я выстрелил в себя и был боевой. Было больно.')
                        revolver.pop(0)
                    elif (gun <= 49) and ((revolver[0] / 2) == 0):
                        print('Я выстрелил в тебя и был боевой. Не повезло тебе.')
                        lifes -= 1
                        revolver.pop(0)
                    elif (gun <= 49) and ((revolver[0] / 2) > 0):
                        print('Я выстрелил в тебя и был холостой. Тебе повезло.')
                        revolver.pop(0)
                    if (gun >= 50) and ((revolver[0] / 2) > 0):
                        print('Я выстрелил в себя и был холостой. Я хожу ещё раз.')
                        revolver.pop(0)
        else:
            print('Ошибка: нужно ввести только либо слова "в себя", либо слова "в тебя".')
            break
        if (choice == 'в себя' or choice == 'В себя') and ((revolver[0] / 2) > 0):
            print('Повезло. Холостой.')
            revolver.pop(0)
    if lifes == 0:
        print('Ты проиграл. Повезёт в следующий раз.')
    elif dealers_lifes == 0:
        print('Ты выирал. Поздравляю!')
else:
    print('Ошибка: нужно ввести только либо слово "да", либо слово "нет"')
