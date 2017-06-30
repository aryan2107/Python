from tkinter import *

def left_click():
    c.delete(ALL)

def right_click():
    c.delete(shape)

root=Tk()

c=Canvas(root,width=300, height=300)
c.pack()

createLine= c.create_line(0,0,100,100)
redline=c.create_line(200,200,100,100,fill='red')

shape=c.create_rectangle(50,50,200,100,fill='green')
oval=c.create_oval(150,150,100,100,fill='blue')
text=c.create_text(20,20,text='THIS IS SAMPLE TEXT',fill='black')

btn1=Button(root,text='left-click',command=left_click)
btn2=Button(root,text='right-click',command=right_click)
btn1.pack(side=BOTTOM)
btn2.pack(side=BOTTOM)


