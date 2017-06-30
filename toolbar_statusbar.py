
from tkinter import *


def donothing():
    print ('IT WORKED')
    
# ***** MENU ********

root=Tk()
root.title(string='LOGIN PAGE')
#root.geometry('640x480')



m=Menu(root)
root.config(menu=m)

submenu=Menu(m)
m.add_cascade(label='File',menu=submenu)
submenu.add_command(label='New File', command=donothing)
submenu.add_command(label='Open', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=donothing)


editmenu=Menu(m)
m.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut',command=donothing)
editmenu.add_command(label='Copy',command=donothing)
editmenu.add_command(label='Paste',command=donothing)
editmenu.add_separator()
editmenu.add_command(label='Exit', command=donothing)

# **** ToolBar *******

toolbar=Frame(root,bg='grey')
toolbar.pack(side=TOP,fill=X)
btn1=Button(toolbar, text='Print', command=donothing)
btn2=Button(toolbar, text='Paste', command=donothing)
btn3=Button(toolbar, text='Cut', command=donothing)
btn4=Button(toolbar, text='Copy', command=donothing)
btn1.pack(side=LEFT,padx=2)
btn2.pack(side=LEFT,padx=2)
btn3.pack(side=LEFT,padx=2)
btn4.pack(side=LEFT,padx=2)
label1=Label(root, text='WELCOME TO MY PAGE', fg='red', bg='blue')
label1.pack()


# **** StatusBar ******************

status= Label(root,text='Loading',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)






