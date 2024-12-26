# importing all of tkinter's functions. 
from tkinter import *

#defining some functions...
def clear():
    display1.delete(0, END)
    display2.delete(0, END)

def insert(num):
    first = display1.get()
    display1.delete(0, END)
    c = str(first) + str(num)
    display1.insert(0, c)

def equal():
    display2.delete(0,END)
    try:
        display2.insert(0, "= " + str(round(float(eval(display1.get())))))
    except ZeroDivisionError:
        display2.insert(0, "= " + "Not Defined")

def exits():
    exit()

def pos_neg():
    if float(display1.get())<0:
        old = display1.get()
        display1.delete(0, END)
        display1.insert(0, old[1:])
    elif float(display1.get()) >0:
        old = display1.get()
        display1.insert(0, "-" + old[1:])
    # can be said as display1.get() >0

def backspace():
    first = display1.get()
    display1.delete(0, END)
    
    display1.insert(0, first[0:len(first)-1])


mode="light"
b = "black"
c = "#5ad1c1"
def mode_change():
    global mode, b
    if mode == "light":
        mode = "dark"
        # APPLYING DARK MODE TO ALL BUTTONS
        for i in names:
            i.configure(fg="white", bg="#1f2140")
        display1.configure(fg="yellow", bg="black")
        display2.configure(fg="yellow", bg="black")
        modes.configure(text = "Light Mode")
    else:
        mode = "light"
        # APPLYING LIGHT MODE TO ALL BUTTONS
        for i in names:
            i.configure(fg="black", bg="#5ad1c1")
        display1.configure(fg="black", bg="white")
        display2.configure(fg="black", bg="white")
        modes.configure(text = "Dark Mode")
   

root = Tk() 
root.configure(background="black")
root.geometry("202x355")
root.resizable(False, False)
#defined and gridded the entry system
display1 = Entry(root, width= 16, font=("Comic Sans MS", 15), borderwidth=4, bg="white", fg="black")
display1.grid(row=0 ,column=0)

display2 = Entry(root, width = 16, font=("Comic Sans MS", 15), borderwidth = 4, bg="white", fg="black")
display2.grid(row = 1, column =0)

# setting the title of the window
root.title("Calculator")

# numbers
# first number row

frame2 = Frame(root, width=195, height =100 )
frame2.grid(row = 2, column=0, columnspan =4)

x=5
y=2

num7 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg=b, text="7", command=lambda:insert(7))
num8 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="8", command=lambda:insert(8))
num9 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="9", command=lambda:insert(9))
addition = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="+", command=lambda:insert("+"))

# second number row 
num4 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="4", command=lambda:insert(4))
num5 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="5", command=lambda:insert(5))
num6 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="6", command=lambda:insert(6))
subtraction = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="-", command=lambda:insert("-"))

# third number row
num1 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="1", command=lambda:insert(1))
num2 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="2",command=lambda:insert(2))
num3 = Button(frame2, width= x, height= y, bg=c, bd = 5,fg="black", text="3", command=lambda:insert(3))
multiplication = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="*", command=lambda:insert("*"))

# fourth number row
num0 = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="0", command=lambda:insert(0))
decimal = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text=".", command=lambda:insert("."))
equal = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="=", command=equal)
division = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="/", command= lambda:insert("/"))

# fifth number row
openbrackets = Button(frame2, width =x, height=y, bg=c, bd = 5,fg="black", text="(", command=lambda:insert("("))
closingbrackets = Button(frame2, width =x, height=y, bg=c, bd = 5,fg="black", text=")", command=lambda:insert(")"))
exits = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="Exit", command=exits)
clear = Button(frame2, width=x, height=y, bg=c, bd = 5,fg="black", text="Clear", command=clear)

frame3 = Frame(root, width=195, height=4)
frame3.grid(row=3, column=0, columnspan = 2)
#sixth number row
pos_neg = Button(frame3, width=5, height=y, bg=c, bd = 5,fg="black", text="+/-", command=pos_neg)
backspace = Button(frame3, width=5, height=y, bg=c, bd = 5,fg="black", text="<--", command=backspace)
modes = Button(frame3, width=12, height = y, bg=c, bd = 5,fg="black", text="Dark Mode", command=mode_change)


names = [num7, num8, num9, num4, num5, num6, num1, num2, num3, num0, decimal, equal, addition,
         subtraction, multiplication, division, openbrackets, closingbrackets, exits, clear, pos_neg, backspace
         , modes]
# button gridding starts
num7.grid(row=2, column=0)
num8.grid(row=2, column=1)
num9.grid(row=2, column=2)
addition.grid(row=2, column=3)

num4.grid(row=3, column=0)
num5.grid(row=3, column=1)
num6.grid(row=3, column=2)
subtraction.grid(row=3, column=3)

num1.grid(row=4, column=0)
num2.grid(row=4, column=1)
num3.grid(row=4, column=2)
multiplication.grid(row=4, column=3)

num0.grid(row=5, column=0)
decimal.grid(row=5, column=1)
equal.grid(row=5, column=2)
division.grid(row=5, column=3)

openbrackets.grid(row=6, column=0)
closingbrackets.grid(row=6, column=1)
exits.grid(row=6, column=2)
clear.grid(row=6, column=3)

pos_neg.grid(row = 0, column= 0)
backspace.grid(row=0, column=1)
modes.grid(row=0, column=2)

root.mainloop()
