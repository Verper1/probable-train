from tkinter import *
from random import *

root = Tk()
root.title('Камень, ножницы, бумага')
root.geometry('500x500')
root.resizable(height=False, width=False)
root['bg'] = 'purple'


def game(player_choice):
    rps = ['Камень', 'Ножницы', 'Бумага']
    computer_choice = choice(rps)
    labelText.configure(text=computer_choice)

    if computer_choice == player_choice:
        labelText.config(text='Ничья!')
    elif (computer_choice == 'Камень' and player_choice == 'Бумага') or \
            (computer_choice == 'Ножницы' and player_choice == 'Камень') or \
            (computer_choice == 'Бумага' and player_choice == 'Ножницы'):
        labelText.config(text='Ты выиграл!')
    elif (computer_choice == 'Бумага' and player_choice == 'Камень') or \
            (computer_choice == 'Камень' and player_choice == 'Ножницы') or \
            (computer_choice == 'Ножницы' and player_choice == 'Бумага'):
        labelText.config(text='ПК выиграл!')
    else:
        labelText.config(text="It's impossible;)")


labelText = Label(root, text='Итог игры...', fg='white', font=('Comic Sans MS', 20), bg='green')
labelText.place(x=200, y=200)

stone = Button(root,
               text='Камень',
               font=('Comic Sans MS', 20),
               bg='green',
               fg='white',
               command=lambda: game('Камень'),
               )
stone.place(x=15, y=400)

scissors = Button(root,
                  text='Ножницы',
                  font=('Comic Sans MS', 20),
                  bg='green',
                  fg='white',
                  command=lambda: game('Ножницы'),
                  )
scissors.place(x=170, y=400)

paper = Button(root,
               text='Бумага',
               font=('Comic Sans MS', 20),
               bg='green',
               fg='white',
               command=lambda: game('Бумага'),
               )
paper.place(x=370, y=400)

root.mainloop()
