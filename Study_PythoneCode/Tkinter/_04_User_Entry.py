from tkinter import *

root = Tk()
myentry = Entry(root, width=50, borderwidth=50)
myentry.focus_set()
myentry.insert(0, 'Enter your name: ')
myentry.pack()


def myClick():
    getentry = myentry.get()
    mylabel = Label(root, text=getentry)
    mylabel.pack()


mybtn = Button(root, text='CLICK ME', padx=10, pady=10, command=myClick)
mybtn.pack()

root.mainloop()
