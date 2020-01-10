from tkinter import *

root = Tk()
root.iconbitmap("D:\Indie\Celeste\Celeste.exe")
root.title("Calculator")

def str_add(a):
    b = output.get()
    output.delete(0, END)
    output.insert(0, b+a)

def equate():
    try:
        ans = eval(output.get())
        output.delete(0, END)
        output.insert(0, ans)
    except Exception:
        output.delete(0, END)
        output.insert(0, "ERROR")

output = Entry(root, borderwidth=5, width=15*3)
output.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
btn9 = Button(root, text="9", height=6, width=15, command=lambda: str_add("9"))
btn9.grid(row=1, column=0, padx=1, pady=1)
btn8 = Button(root, text="8", height=6, width=15, command=lambda: str_add("8"))
btn8.grid(row=1, column=1, padx=1, pady=1)
btn7 = Button(root, text="7", height=6, width=15, command=lambda: str_add("7"))
btn7.grid(row=1, column=2, padx=1, pady=1)
btn6 = Button(root, text="6", height=6, width=15, command=lambda: str_add("6"))
btn6.grid(row=2, column=0, padx=1, pady=1)
btn5 = Button(root, text="5", height=6, width=15, command=lambda: str_add("5"))
btn5.grid(row=2, column=1, padx=1, pady=1)
btn4 = Button(root, text="4", height=6, width=15, command=lambda: str_add("4"))
btn4.grid(row=2, column=2, padx=1, pady=1)
btn3 = Button(root, text="3", height=6, width=15, command=lambda: str_add("3"))
btn3.grid(row=3, column=0, padx=1, pady=1)
btn2 = Button(root, text="2", height=6, width=15, command=lambda: str_add("2"))
btn2.grid(row=3, column=1, padx=1, pady=1)
btn1 = Button(root, text="1", height=6, width=15, command=lambda: str_add("1"))
btn1.grid(row=3, column=2, padx=1, pady=1)
btn0 = Button(root, text="0", height=6, width=15, command=lambda: str_add("0"))
btn0.grid(row=4, column=0, padx=1, pady=1)
btnClear = Button(root, text="Clear", height=6, width=15, command=lambda: output.delete(0, END))
btnClear.grid(row=4, column=1, padx=1, pady=1)
btnAdd = Button(root, text='+', height=6, width=15, command=lambda: str_add("+"))
btnAdd.grid(row=4, column=2, padx=1, pady=1)
btnSub = Button(root, text='-', height=6, width=15, command=lambda: str_add("-"))
btnSub.grid(row=5, column=0, padx=1, pady=1)
btnMul = Button(root, text='*', height=6, width=15, command=lambda: str_add("*"))
btnMul.grid(row=5, column=1, padx=1, pady=1)
btnDiv = Button(root, text='/', height=6, width=15, command=lambda: str_add("/"))
btnDiv.grid(row=5, column=2, padx=1, pady=1)
btnBrac1 = Button(root, text='(', height=6, width=15, command=lambda: str_add("("))
btnBrac1.grid(row=6, column=0, padx=1, pady=1)
btnBrac2 = Button(root, text=')', height=6, width=15, command=lambda: str_add(")"))
btnBrac2.grid(row=6, column=1, padx=1, pady=1)
btnPow = Button(root, text='Pow', height=6, width=15, command=lambda: str_add("**"))
btnPow.grid(row=6, column=2, padx=1, pady=1)
btnEq = Button(root, text='=', height=6, width=15*3+4, command=equate)
btnEq.grid(row=7, column=0, columnspan=3, padx=1, pady=1)






root.mainloop()