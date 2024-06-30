# 1. Угадай число – компьютер выберет случайное число, а игроки должны будут по очереди угадывать число.
# При разработке используются: генератор случайных чисел, цикл while, условные конструкции if/else,
# переменные, целые числа и вывод на экран.

import random

number = random.randint(1, 10)
rounds = 1
used_numbers = set()

answer = input('Do you want to play a game? Your answer is: ').lower()
if answer == 'yes':
    print('''
    You would play a game that called "Guess a number". That game require two players. 
    AI wil generate a number and players must guess it. The players take turns walking.
    Game will end if one of the players would guess correct number. 
    Number can only be an integer and in range from 1 to 10.''')

    while rounds != 0:
        guess_pl1 = int(input('''
Guess a number, player 1: '''))
        if guess_pl1 == number:
            print(f'You win, player 1! AI generated that number: {number}')
            rounds -= 1
        else:
            print('Incorrect guess, player 1.')
            used_numbers.add(guess_pl1)
            guess_pl2 = int(input('Your turn, player 2: '))
            if guess_pl2 == number:
                print(f'You win, player 2! AI generated that number: {number}')
                rounds -= 1
            else:
                print('Incorrect guess, player 2.')
                used_numbers.add(guess_pl2)
                print(f'Used numbers: {used_numbers}')

elif answer == 'no':
    print('Then why are you here?')
else:
    print('Error: you can enter word "yes" and "no" only')
