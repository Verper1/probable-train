# Виселица – продвинутый вариант «угадай число». Игрок должен угадывать буквы в загаданном слове. Для упрощенной
# версии используйте только текст, без графики. Потребуется опыт работы со списками, генератор случайных чисел, работа
# со строками, обработка ввода, вывод, цикл while, операторы if/else. Для списка слов воспользуйтесь словарем Sowpods.

import random


def game():

    word = random.choice(['sheep', 'rat', 'dawn', 'foot', 'tree'])
    # print(word)
    words_letters = set([i for i in word])
    # print(words_letters)
    print('''
Hello! You will play that name is 'The Gallows'. You'll need to guess a word by entering letter. If word
have this letter then it will appear. if word haven't entered letter then 1 life would be taken. You have 3 lives.
Good luck!
''')

    hidden_word = ['_'] * len(word)
    # print(hidden_word)
    print(' '.join(hidden_word))

    cor_letters = 0
    lives = 3

    while True:
        if lives == 0:
            print('Game over. No more lives left.')
            break
        if cor_letters == len(word):
            print(f'You are win. Congratulations!. The correct word is {word}')
            break

        answer = input('''
Enter letter: ''').lower().strip().replace(' ', '')

        if answer in hidden_word or len(answer) > 1:
            print('You already entered that letter!')
            continue
        if answer in words_letters:
            for i in range(len(word)):
                if word[i] == answer:
                    hidden_word[i] = answer
                    cor_letters += 1
            print(' '.join(hidden_word))
            # print(hidden_word)
        else:
            lives -= 1
            print(f'Incorrect letter! You have {lives} lives left.')
            print(' '.join(hidden_word))


if __name__ == '__main__':
    answer = input('Do you want to play a game? Your answer is: ').lower().strip().replace(' ', '')
    if answer == 'yes':
        game()
        while True:
            sequel = (input('Do you wanna play one more time in this game? Your answer is: ').lower().strip()
                      .replace(' ', ''))
            if sequel == 'yes':
                game()
            elif sequel == 'no':
                print('OK. See you next time!')
                break
            else:
                print('Error: you can enter word "yes" and "no" only')
    elif answer == 'no':
        print('Then why are you here?')
    else:
        print('Error: you can enter word "yes" and "no" only')
