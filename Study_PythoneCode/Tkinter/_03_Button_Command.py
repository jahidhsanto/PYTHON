from tkinter import *

root = Tk()

x = 0


def myButton():
    global x
    mylabel = Label(root, text='Its working')
    mylabel.grid(row=x, column=1)
    x = x + 1


mybtn = Button(root, text='CLICK ME', fg='red', bg='green', padx=50, pady=20, command=myButton)
mybtn.grid(row=0, column=0)

root.mainloop()
