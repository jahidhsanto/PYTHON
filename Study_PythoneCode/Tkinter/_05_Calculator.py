from tkinter import *

# This section is for Frame ==============================================================
root = Tk()  # create a root widget
root.title("CALCULATOR")
root.configure(background="black")
root.minsize(450, 520)  # width, height
# root.maxsize(450, 520)
root.geometry("550x520+800+50")  # width x height + x + y
# This section is for Frame ==============================================================


# This section is for Panel ==============================================================
dspPanel = Label(root, width=450)
dspPanel.pack()
btnPanel = Label(root, width=400, height=450)
btnPanel.pack()
# This section is for Panel ==============================================================


# This section is for EntryPanel ==============================================================
myentry = Entry(dspPanel, width=23, borderwidth=10, font=("Digital-7", 36), justify=RIGHT)
myentry.pack()
myentry.focus_set()


# This section is for EntryPanel ==============================================================


# This section for button Action ==============================================================
def button_click(number):
    myentry.insert(len(myentry.get()), number)


def button_clear():
    myentry.delete(0, END)


def button_OPP(op):
    match op:
        case '+':
            myentry.insert(len(myentry.get()), ' ' + '+' + ' ')
        case '-':
            myentry.insert(len(myentry.get()), ' ' + '-' + ' ')
        case '*':
            myentry.insert(len(myentry.get()), ' ' + '*' + ' ')
        case '/':
            myentry.insert(len(myentry.get()), ' ' + '/' + ' ')
        case '%':
            myentry.insert(len(myentry.get()), ' ' + '%' + ' ')


# def button_Equal():
#     x = myentry.get().split(' + ')
#     sum = 0
#     for y in range(len(x)):
#         try:
#             sum = sum + int(x[y])
#             myentry.delete(0, END)
#             myentry.insert(0, sum)
#         except:
#             myentry.delete(0, END)
#             myentry.insert(0, 'MATH ERROR')
#             break

def button_Equal():
    x = myentry.get().split(' ')
    try:
        a = float(x[0])
        b = float(x[2])

        match x[1]:
            case '+':
                myentry.delete(0, END)
                myentry.insert(0, a + b)
            case '-':
                myentry.delete(0, END)
                myentry.insert(0, a - b)
            case '*':
                myentry.delete(0, END)
                myentry.insert(0, a * b)
            case '/':
                myentry.delete(0, END)
                myentry.insert(0, a / b)
            case '%':
                myentry.delete(0, END)
                myentry.insert(0, a % b)
    except:
        myentry.delete(0, END)
        myentry.insert(0, 'MATH ERROR')


# This section for button Action ==============================================================

# This section for button Panel ==============================================================
btn7 = Button(btnPanel, text='7', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(7))
btn8 = Button(btnPanel, text='8', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(8))
btn9 = Button(btnPanel, text='9', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(9))
btn4 = Button(btnPanel, text='4', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(4))
btn5 = Button(btnPanel, text='5', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(5))
btn6 = Button(btnPanel, text='6', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(6))
btn1 = Button(btnPanel, text='1', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(1))
btn2 = Button(btnPanel, text='2', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(2))
btn3 = Button(btnPanel, text='3', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_click(3))
btn0 = Button(btnPanel, text='0', padx=83, pady=20, font=("Roboto", 24), command=lambda: button_click(0))
btnDot = Button(btnPanel, text='.', padx=35, pady=20, font=("Roboto", 24), command=lambda: button_click('.'))

btnAdd = Button(btnPanel, text='+', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_OPP('+'))
btnSub = Button(btnPanel, text='-', padx=32, pady=20, font=("Roboto", 24), command=lambda: button_OPP('-'))
btnMul = Button(btnPanel, text='*', padx=33, pady=20, font=("Roboto", 24), command=lambda: button_OPP('*'))
btnDiv = Button(btnPanel, text='/', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_OPP('/'))
btnMod = Button(btnPanel, text='%', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_OPP('%'))

btnEqual = Button(btnPanel, text='=', padx=85, pady=20, font=("Roboto", 24), command=lambda: button_Equal())
btnClear = Button(btnPanel, text='C', padx=30, pady=20, font=("Roboto", 24), command=lambda: button_clear())

btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btnMod.grid(row=0, column=3)
btnClear.grid(row=0, column=4)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btnMul.grid(row=1, column=3)
btnDiv.grid(row=1, column=4)

btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btnAdd.grid(row=2, column=3)
btnSub.grid(row=2, column=4)

btn0.grid(row=3, column=0, columnspan=2)
btnDot.grid(row=3, column=2)
btnEqual.grid(row=3, column=3, columnspan=2)
# This section for button Panel ==============================================================

root.mainloop()
