# 3. Генератор MadLibs – игра, в которой в пробелы нужно вставлять глупые слова, а после зачитывать.
# Для реализации понадобится понимание строк, переменных, конкатенация, ввод данных и вывод.

answer = input('Do you want to play a game? Your answer is: ').lower().strip()
if answer == 'yes':

    print('''
    You would play a game that called "Guess a number". In this game you need to insert words into spaces. 
    At the end, the program will voice the text. Let\'s begin!
    ''')
    adjective = input('adjective: ').lower().strip()
    name = input('child\'s name: ').strip()
    verb_ing = input('verb ending in -ing: ').lower().strip()
    boy_girl = input('he/she: ').lower().strip()
    adjective_2 = input('adjective: ').lower().strip()
    adjective_3 = input('adjective: ').lower().strip()
    noun = input('noun: ').lower().strip()
    print(f'''
    One {adjective} night, {name} was {verb_ing} in the backyard when {boy_girl} saw a(n) {adjective_2} 
    light in the sky. It got bigger and bigger until a(n) {adjective_3} spaceship landed right next to the {noun}!
    ''')

elif answer == 'no':
    print('Then why are you here?')
else:
    print('Error: you can enter word "yes" and "no" only')
