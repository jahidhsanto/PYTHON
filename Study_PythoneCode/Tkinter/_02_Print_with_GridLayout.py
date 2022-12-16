from tkinter import *

root = Tk()
root.title('Python Tkinter')

label1 = Label(root, text='Label 1')
label2 = Label(root, text='Label 2')
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

root.mainloop()
