from tkinter import *

root = Tk()  # create a root widget
root.title("CALCULATOR")
root.configure(background="yellow")
root.minsize(450, 520)  # width, height
root.maxsize(450, 520)
root.geometry("450x520+800+50")  # width x height + x + y

dspPanel = Label(root, width=400)
dspPanel.pack()
btnPanel = Label(root, width=400, height=450)
btnPanel.pack()

# for display
myentry = Entry(dspPanel, width=18, borderwidth=10, font=("Digital-7", 36), justify=RIGHT)
myentry.pack()
myentry.focus_set()


def button_click(number):
    myentry.insert(len(myentry.get()), number)


def button_clear():
    myentry.delete(0, END)


arr = []


def button_Add():
    myentry.insert(len(myentry.get()), ' ' + '+' + ' ')
    # print(type(myentry.get()))
    # arr.append(myentry.get())


sum = 0


def button_Equal():
    x = myentry.get().split(' + ')

    sum = 0
    for y in range(len(x)):
        try:
            sum = sum + int(x[y])
            myentry.delete(0, END)
            myentry.insert(0, sum)
        except:
            myentry.delete(0, END)
            myentry.insert(0, 'MATH ERROR')
            break


# for button
btn7 = Button(btnPanel, text='7', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(7))
btn8 = Button(btnPanel, text='8', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(8))
btn9 = Button(btnPanel, text='9', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(9))
btn4 = Button(btnPanel, text='4', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(4))
btn5 = Button(btnPanel, text='5', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(5))
btn6 = Button(btnPanel, text='6', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(6))
btn1 = Button(btnPanel, text='1', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(1))
btn2 = Button(btnPanel, text='2', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(2))
btn3 = Button(btnPanel, text='3', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(3))
btn0 = Button(btnPanel, text='0', padx=135, pady=20, font=("Roboto", 24), command=lambda: button_click(0))
btnAdd = Button(btnPanel, text='+', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_Add())
btnEqual = Button(btnPanel, text='=', padx=30, pady=75, font=("Roboto", 24), command=lambda: button_Equal())
btnClear = Button(btnPanel, text='C', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_clear())

btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btn0.grid(row=3, column=0, columnspan=3)
btnClear.grid(row=0, column=3)
btnAdd.grid(row=1, column=3)
btnEqual.grid(row=2, column=3, rowspan=2)

root.mainloop()
