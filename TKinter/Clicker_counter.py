from tkinter import *

root = Tk()

root.title('Счётчик кликов')
root.geometry('200x200')
root.resizable(height=False, width=False)

click = 0


def click_counter():
    global click
    click += 1
    label.configure(text=click)


label = Label(root,
              text='0',
              font='Arial 35',
              )
label.pack()

btn = Button(root,
             text='Кликай давай',
             padx='25',
             pady='25',
             command=click_counter,
             bg='yellow'
             )
btn.pack()


root.mainloop()
