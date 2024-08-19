from tkinter import *

root = Tk()
root.title('Alarm')

# root.config(bg='black')
root['bg'] = 'lime'

label = Label(root,
              text='Text',
              font=("Comic Sans MS", 20, 'italic'),
              bg='yellow',
              activebackground='red',
              activeforeground='white',
              fg='cyan'
              )

label.pack()

img = PhotoImage(file='icons8-будильник-50.png')
l_pic = Label(root, image=img)
l_pic.pack()

root.geometry('1024x768')
root.resizable(width=False, height=False)

root.mainloop()
