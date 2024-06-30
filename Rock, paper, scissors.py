# 2. Камень, ножницы, бумага – мини-игра, в которую можно играть в одиночку с компьютером.
# При разработке потребуются знания генератора случайных чисел, вывод на экран, обработка ввода,
# цикл while и оператор if/else.

import random

rounds = 3
wins_pl = 0
wins_AI = 0
AI_respond = ''

answer = input('Do you want to play a game? Your answer is: ').lower()
if answer == 'yes':
    print('''
    You would play a game that called "Rock, paper, scissors". In this game you will play with AI.
    This game have 3 rounds. If one of you win 2 times in a row then that person would be a winner.
    You need to write word "paper" or "rock" or "scissors" in console and AI will respond you with his word.
    Other rules that game you already know. Good luck!''')

    while rounds != 0:
        if wins_AI == 2:
            print('''
AI wins! Better next time.''')
            break
        elif wins_pl == 2:
            print('''
Players wins! Congratulations.''')
            break
        AI_respond = random.randint(0,  2)  # 0 = rock, 1 = paper, 2 = scissors
        if AI_respond == 0:
            AI_respond = 'rock'
        elif AI_respond == 1:
            AI_respond = 'paper'
        else:
            AI_respond = 'scissors'
        word_pl = input('''
Enter word: ''').lower().strip()
        if word_pl not in ['rock', 'paper', 'scissors']:
            print('Error: invalid input. Rock, paper, scissors only. Try again.')
            continue
        print(f'AI respond is {AI_respond}.')

        if word_pl == 'paper' and AI_respond == 'rock':
            wins_pl += 1
            rounds -= 1
            print('Player wins.')
        elif word_pl == 'paper' and AI_respond == 'paper':
            print('Draw. This round will be reset')
            continue
        elif word_pl == 'paper' and AI_respond == 'scissors':
            wins_AI += 1
            rounds -= 1
            print('AI wins')
        if word_pl == 'rock' and AI_respond == 'rock':
            print('Draw. This round will be reset')
            continue
        elif word_pl == 'rock' and AI_respond == 'paper':
            wins_AI += 1
            rounds -= 1
            print('AI wins')
        elif word_pl == 'rock' and AI_respond == 'scissors':
            wins_pl += 1
            rounds -= 1
            print('Player wins.')
        if word_pl == 'scissors' and AI_respond == 'scissors':
            print('Draw. This round will be reset')
            continue
        elif word_pl == 'scissors' and AI_respond == 'rock':
            wins_AI += 1
            rounds -= 1
            print('AI wins')
        elif word_pl == 'scissors' and AI_respond == 'paper':
            wins_pl += 1
            rounds -= 1
            print('Player wins.')
        else:
            continue

elif answer == 'no':
    print('Then why are you here?')
else:
    print('Error: you can enter word "yes" and "no" only')

# import random
#
#
# def play_game():
#     rounds = 3
#     wins_pl = 0
#     wins_ai = 0
#
# print('''
# You would play a game that called "Rock, paper, scissors". In this game you will play with AI.
# This game have 3 rounds. If one of you win 2 times in a row then that person would be a winner.
# You need to write word "paper" or "rock" or "scissors" in console and AI will respond you with his word.
# Other rules that game you already know. Good luck!''')
#
# while rounds != 0:
#     if wins_ai == 2:
#         print('AI wins! Better next time.')
#         break
#     elif wins_pl == 2:
#         print('Player wins! Congratulations.')
#         break
#
#     word_pl = input('Enter word: ').lower().strip()
#     if word_pl not in ['rock', 'paper', 'scissors']:
#         print('Invalid input. Please enter "rock", "paper", or "scissors".')
#         continue

#         word_ai = random.choice(['rock', 'paper', 'scissors'])
#         print(f'AI responds with: {word_ai}')
#
# if word_pl == word_ai:
#     print('Draw. This round will be reset')
#         elif (word_pl == 'rock' and word_ai == 'scissors') or \
#              (word_pl == 'paper' and word_ai == 'rock') or \
#              (word_pl == 'scissors' and word_ai == 'paper'):
#             print('Player wins.')
#             wins_pl += 1
#             rounds -= 1
#         else:
#             print('AI wins')
#             wins_ai += 1
#             rounds -= 1
#
#
# if __name__ == '__main__':
#     answer = input('Do you want to play a game? Your answer is: ').lower()
#     if answer == 'yes':
#         play_game()
#     elif answer == 'no':
#         print('Then why are you here?')
#     else:
#         print('Error: you can enter word "yes" and "no" only')
