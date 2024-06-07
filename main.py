from tkinter import *
import tkinter as tk

        
root=Tk()
root.title("CALCULATOR")
root.geometry("500x200")

equation_text=""
equation_label=StringVar()

label=Label(root,bg='skyblue',textvariable=equation_label,relief=SUNKEN,borderwidth=3,width=50)
label.pack()
frame = Frame(root)
frame.pack()
def press(num):
    global equation_text
    equation_text=equation_text+ str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    try:
        total= str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except ZeroDivisionError:
        equation_label.set("Arithmetic error")
        equation_text=""
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text=""
def clear():
    global equation_text
    equation_label.set("")
    equation_text=""
    
#BUTTONS 123
but1=Button(frame,text='1',fg='black',bg='red', command=lambda:press(1),height=1,width=7)
but1.grid(row=2,column=0)

but2=Button(frame,text='2',fg='black',bg='red',command=lambda:press(2),height=1,width=7)
but2.grid(row=2,column=1,pady=2)

but3=Button(frame,text='3',fg='black',bg='red',command=lambda:press(3),height=1,width=7)
but3.grid(row=2,column=3,pady=2)

but4=Button(frame,text='4',fg='black',bg='red', command=lambda:press(4),height=1,width=7)
but4.grid(row=3,column=0,pady=2)

but5=Button(frame,text='5',fg='black',bg='red',command=lambda:press(5),height=1,width=7)
but5.grid(row=3,column=1,pady=2)

but6=Button(frame,text='6',fg='black',bg='red',command=lambda:press(6),height=1,width=7)
but6.grid(row=3,column=3,pady=2)

but7=Button(frame,text='7',fg='black',bg='red', command=lambda:press(7),height=1,width=7)
but7.grid(row=4,column=0,pady=2)

but8=Button(frame,text='8',fg='black',bg='red',command=lambda:press(8),height=1,width=7)
but8.grid(row=4,column=1,pady=2)

but9=Button(frame,text='9',fg='black',bg='red',command=lambda:press(9),height=1,width=7)
but9.grid(row=4,column=3,pady=2)

but0=Button(frame,text='0',fg='black',bg='red',command=lambda:press(0),height=1,width=7)
but0.grid(row=5,column=0,pady=2)
label=Label(frame,text='BY HARMAN SOHAL',bg='black',fg='yellow')
label.grid(row=6,column=10)

##operatorsbuttons

butp=Button(frame,text='+',fg='black',bg='red',command=lambda:press('+'),height=1,width=7)
butp.grid(row=2,column=5)

buts=Button(frame,text='-',fg='black',bg='red',command=lambda:press('-'),height=1,width=7)
buts.grid(row=3,column=5)
butm=Button(frame,text='*',fg='black',bg='red',command=lambda:press('*'),height=1,width=7)
butm.grid(row=4,column=5)
butd=Button(frame,text='/',fg='black',bg='red',command=lambda:press('/'),height=1,width=7)
butd.grid(row=5,column=5)
equalto=Button(frame,text='=',command=lambda:equals())
equalto.grid(row=6,column=5)

decimal=Button(frame,text='.',fg='black',bg='red',command=lambda:press('.'),height=1,width=7)
decimal.grid(row=6,column=1)

clear=Button(frame,text='clear',fg='black',bg='red',command=clear,height=1,width=7)
clear.grid(row=6,column=0,pady=2)
  
root.mainloop()