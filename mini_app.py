from tkinter import *


class App():

    def __init__(self,master):
        self.master=master
        self.master.title(string='MY APPLICATION')
        self.frame=Frame(self.master,bg='black')
        self.frame.grid()
        self.button=Button(self.frame,text='Click Me',command=self.display)
        self.button.grid(row=3,column=5,padx=2)
        self.entry=Entry(self.frame)
        self.output=self.entry.get()
        self.entry.grid(row=3,column=3)

    def display(self):
        print ('self.entry contains', self.output)
        label=Label(self.frame,text=self.output,bg='blue')
        label.grid(row=4,column=3)
        
       
    

root = Tk()
app=App(root)
root.mainloop()
