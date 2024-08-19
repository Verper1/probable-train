from tkinter import *


root = Tk()
root.title('Alarmclock')
root.iconbitmap('alarmclock_pic.ico')

# root.config(bg='black')
root['bg'] = 'lime'


def click():
    print('Button')


btn = Button(root,
             text='Button',  # сам текст кнопки
             command=click,  # то, что запускает кнопка
             font=("Comic Sans MS", 20, 'italic'),  # шрифт, кегли и начертание
             bg='yellow',  # фон кнопки
             activebackground='red',  # фон активированной кнопки
             activeforeground='white',  # текст активированной кнопки
             fg='cyan'  # цвет текста до активации
             )
btn.pack()

root.geometry('1024x768')
root.resizable(width=False, height=False)

root.mainloop()
