from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self,root):
        self.root=root
        self.root.title('To Do List')
        self.root.geometry('650x410+300+150')

        self.label=Label(root,text="To Do List",font='ariel,25,bold',width=10,bd=5,bg='black',fg='yellow')
        self.label.pack(side='top',fill=BOTH)
        self.label2=Label(root,text="ADD TASK",font='ariel,25,bold',width=10,bd=5,bg='black',fg='yellow')
        self.label2.place(x=40,y=54)
        self.label3=Label(root,text="Tasks",font='ariel,25,bold',width=10,bd=5,bg='black',fg='yellow')
        self.label3.place(x=320,y=54)
        self.listbox=Listbox(root,height=8,bd=5,width=23,font='ariel,20,bold')
        self.listbox.place(x=300,y=100)
        self.text=Text(root,bd=5,height=2,width=22,font='ariel,10,bold')
        self.text.place(x=20,y=120)
        self.button=Button(root,text="ADD",font='ariel,25,bold',width=10,bd=5,bg='black',fg='yellow',command=lambda:add())
        self.button.place(x=40,y=220)
        self.button2=Button(root,text="DELETE",font='ariel,25,bold',width=10,bd=5,bg='black',fg='yellow',command=lambda:delete())
        self.label11=Label(root,text='Project by Harman Sohal',font='ariel,25,bold',width=20,bd=5,bg='black',fg='yellow')
        self.label11.place(x=300,y=350)
        self.button2.place(x=40,y=350)
        def add():
            content=self.text.get(1.0,END)
            self.listbox.insert(END,content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
                self.text.delete(1.0,END)
        
        def delete():
            delete_=self.listbox.curselection()
            look=self.listbox.get(delete_)
            with open('data.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
                self.listbox.delete(delete_)
            with open('data.txt','r') as file:
                read=file.readlines()
                for i in read:
                    ready=i.split()
                    self.listbox.insert(END,ready)
                file.close()

def main():
    root=Tk()
    ui=todo(root)
    root.mainloop()
if __name__=="__main__":
    main()
        