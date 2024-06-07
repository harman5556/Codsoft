from tkinter import *
import random,string
class password:
    def __init__(self,root):        
        self.root=root

        self.root.geometry("400x300")
        self.root.title("PASSWORD GENERATOR")

        self.title=StringVar()
        self.label=Label(root,textvariable=self.title).pack()
        self.title.set("The Strength of Password:")
        def select():
            select=choice.get()
        choice=IntVar()
        self.B1=Radiobutton(root,text="EASY",variable=choice,value=1,command=lambda:select).pack(anchor=CENTER)
        self.B2=Radiobutton(root,text="MEDIUM",variable=choice,value=2,command=lambda:select).pack(anchor=CENTER)
        self.B3=Radiobutton(root,text="HARD",variable=choice,value=3,command=lambda:select).pack(anchor=CENTER)
        self.labelchoice=Label(root)
        self.labelchoice.pack()

        self.length=StringVar()
        self.length.set("Password length")
        self.lengthtitle=Label(root,textvariable=self.length).pack()

        self.val=IntVar()
        self.box=Spinbox(root, from_=8, to_=25, textvariable=self.val, width=13).pack()

        def call():
            self.sum.config(text=passwordgen())
        self.button=Button(root,text="GENERATE PASSWORD",bd=5,height=2,command=call).pack()
        self.password=str(call)
        self.sum=Label(root,text="")
        self.sum.pack(side=BOTTOM)

        EASY= string.ascii_uppercase + string.ascii_lowercase
        MEDIUM=string.ascii_uppercase + string.ascii_lowercase + string.digits

        HARD= EASY+MEDIUM

        def passwordgen():
            if choice.get()==1:
                return"".join(random.sample(EASY,self.val.get()))
            elif choice.get()==2:
                return"".join(random.sample(MEDIUM,self.val.get()))
            elif choice.get()==3:
                return"".join(random.sample(HARD,self.val.get()))

        
root=Tk()
password(root)     
root.mainloop()