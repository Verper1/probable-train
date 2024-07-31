import random

gaming_field = list(range(1, 10))


def print_board():
    print("\n---------")
    print(f"{gaming_field[0]} | {gaming_field[1]} | {gaming_field[2]}")
    print("---------")
    print(f"{gaming_field[3]} | {gaming_field[4]} | {gaming_field[5]}")
    print("---------")
    print(f"{gaming_field[6]} | {gaming_field[7]} | {gaming_field[8]}")
    print("---------")


# def game_mode():
#     mode = int(input('Choose a game mode(1 - player/player, 2 - player/PC): '))
#     return mode


respond = '1'


def victory():
    global respond
    
    if (gaming_field[0] == 'X' and gaming_field[1] == 'X' and gaming_field[2] == 'X') or \
            (gaming_field[3] == 'X' and gaming_field[4] == 'X' and gaming_field[5] == 'X') or \
            (gaming_field[6] == 'X' and gaming_field[7] == 'X' and gaming_field[8] == 'X') or \
            (gaming_field[0] == 'X' and gaming_field[4] == 'X' and gaming_field[8] == 'X') or \
            (gaming_field[6] == 'X' and gaming_field[4] == 'X' and gaming_field[2] == 'X') or \
            (gaming_field[0] == 'X' and gaming_field[3] == 'X' and gaming_field[6] == 'X') or \
            (gaming_field[1] == 'X' and gaming_field[4] == 'X' and gaming_field[7] == 'X') or \
            (gaming_field[2] == 'X' and gaming_field[5] == 'X' and gaming_field[8] == 'X'):
        # print('X')
        respond = 'X'
        return respond
        
    elif (gaming_field[0] == 'O' and gaming_field[1] == 'O' and gaming_field[2] == 'O') or \
         (gaming_field[3] == 'O' and gaming_field[4] == 'O' and gaming_field[5] == 'O') or \
         (gaming_field[6] == 'O' and gaming_field[7] == 'O' and gaming_field[8] == 'O') or \
         (gaming_field[0] == 'O' and gaming_field[4] == 'O' and gaming_field[8] == 'O') or \
         (gaming_field[6] == 'O' and gaming_field[4] == 'O' and gaming_field[2] == 'O') or \
         (gaming_field[0] == 'O' and gaming_field[3] == 'O' and gaming_field[6] == 'O') or \
         (gaming_field[1] == 'O' and gaming_field[4] == 'O' and gaming_field[7] == 'O') or \
         (gaming_field[2] == 'O' and gaming_field[5] == 'O' and gaming_field[8] == 'O'):
        # print('O')
        respond = 'O'
        return respond


def player_to_player():
    pl_1 = random.choice(['X', 'O'])
    
    counter = 0
    status = True
    
    if pl_1 == 'X':
        pl_2 = 'O'
    else:
        pl_2 = 'X'

    while True:
        choice_pl_1 = int(input('\nEnter number, player 1: '))
        
        for i in gaming_field:
            if choice_pl_1 == i:
                gaming_field[i - 1] = pl_1
                print_board()
                counter += 1
                victory()
                # print(respond)
        if counter == 9:
            print('\nDraw')
            break
        elif respond == 'O' and pl_1 == 'O':
            print('\nPlayer 1 win!')
            break
        elif respond == 'O' and pl_2 == 'O':
            print('\nPlayer 2 win!')
            break
        elif respond == 'X' and pl_1 == 'X':
            print('\nPlayer 1 win!')
            break
        elif respond == 'X' and pl_2 == 'X':
            print('\nPlayer 2 win!')
            break
    # print(counter) 

        choice_pl_2 = int(input('\nEnter number, player 2: '))
        
        for i in gaming_field:
            if choice_pl_2 == i:
                gaming_field[i - 1] = pl_2
                print_board()
                counter += 1
                victory()
        if counter == 9:
            print('\nDraw')
            break
        elif respond == 'O' and pl_1 == 'O':
            print('\nPlayer 1 win!')
            break
        elif respond == 'O' and pl_2 == 'O':
            print('\nPlayer 2 win!')
            break
        elif respond == 'X' and pl_1 == 'X':
            print('\nPlayer 1 win!')
            break
        elif respond == 'X' and pl_2 == 'X':
            print('\nPlayer 2 win!')
            break


# print(counter) 


def tic_tac_toe():
    pl_1 = random.choice(['X', 'O'])
    if pl_1 == 'X':
        pl_2 = 'O'
    else:
        pl_2 = 'X'

    print(f''' 
Hi! Now you're going to play the Tic-Tac-Toe game. There will be a field in front of you on which you will need to put 
either a zero or a cross, depending on who will walk with what. You're going to play with a robot. 
If someone can line up (diagonally also counts) 3 identical pieces, then that player wins. Good luck! 
Player 1 - {pl_1}, player 2 - {pl_2}. 
''')
    print_board()
    player_to_player()


tic_tac_toe()
