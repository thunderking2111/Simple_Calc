from tkinter import *

ans = 0
preop = ''
newValue = False

def digitClick(digit):
    global ebox
    global newValue

    if newValue:
        ebox.delete(0, END)
        newValue = False

    s = ebox.get()
    s += str(digit)
    ebox.delete(0, END)
    ebox.insert(0, s)

def operation(op):
    global ans
    global preop
    global newValue
    newValue = True
    digit = int(ebox.get())

    if preop == '+':
        ans += digit
    elif preop == '-':
        ans -= digit
    elif preop == '*':
        ans *= digit
    elif preop == '/':
        ans /= digit
        ans = int(ans)
    else:
        ans += digit
        ebox.delete(0, END)

    ebox.delete(0, END)
    ebox.insert(0, str(ans))

    if op == '=':
        preop = ''
        ans = 0
    elif op == 'CE':
        preop = ''
        ans = 0
        ebox.delete(0, END)
    else: 
        preop = op

root = Tk()
root.title("My Calc")
try:
    root.iconbitmap("Calc_Ico.ico")
except:
    pass

ebox = Entry(root, width=55, borderwidth=5)
ebox.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

Button(root, text='0', padx=35, pady=25, command=lambda: digitClick(0)).grid(row=4, column=0)
Button(root, text='1', padx=35, pady=25, command=lambda: digitClick(1)).grid(row=3, column=0)
Button(root, text='2', padx=35, pady=25, command=lambda: digitClick(2)).grid(row=3, column=1)
Button(root, text='3', padx=35, pady=25, command=lambda: digitClick(3)).grid(row=3, column=2)
Button(root, text='4', padx=35, pady=25, command=lambda: digitClick(4)).grid(row=2, column=0)
Button(root, text='5', padx=35, pady=25, command=lambda: digitClick(5)).grid(row=2, column=1)
Button(root, text='6', padx=35, pady=25, command=lambda: digitClick(6)).grid(row=2, column=2)
Button(root, text='7', padx=35, pady=25, command=lambda: digitClick(7)).grid(row=1, column=0)
Button(root, text='8', padx=35, pady=25, command=lambda: digitClick(8)).grid(row=1, column=1)
Button(root, text='9', padx=35, pady=25, command=lambda: digitClick(9)).grid(row=1, column=2)

Button(root, text='=', padx=35, pady=25, command=lambda: operation('=')).grid(row=4, column=1)
Button(root, text='CE', padx=31, pady=25, command=lambda: operation('CE')).grid(row=4, column=2)
Button(root, text='+', padx=35, pady=25, command=lambda: operation('+')).grid(row=1, column=3)
Button(root, text='-', padx=35, pady=25, command=lambda: operation('-')).grid(row=2, column=3)
Button(root, text='x', padx=35, pady=25, command=lambda: operation('*')).grid(row=3, column=3)
Button(root, text='/', padx=35, pady=25, command=lambda: operation('/')).grid(row=4, column=3)

status = Label(root, text="Rahul Prajapati", bd=0.5, relief=SUNKEN, anchor=E)
status.grid(row=5, column=0, columnspan=4,pady=5, sticky=W+E)
mainloop()