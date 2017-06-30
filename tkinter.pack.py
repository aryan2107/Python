# FOLLOWING EXAMPLE USES TKINTER USING PACK MODULE AND NOT GRID MODULE

from tkinter import *

# tkinter is used in python 3 while Tkinter is used in python 2.7
# This is Universal import. It imports all the CLASS from tkinter module.

root = Tk()
root.title(string='SAMPLE WIDGET')
#root.geometry('640x480')

# THIS IS SAME AS tkinter.tk(), when you import tkinter. This initializes TK and creates a small window.

label=Label(root,text='THIS IS SAMPLE TEXT',bg='red',fg='white')
label.pack()
# THE BELOW LABEL WILL BE STRETCHED IN THE X DIRECTION EVEN U STRETCH/DRAG THE WINDOW.
label2=Label(root,text='THIS IS A LONG PIECE OF TEXT TO STRETCH THE WINDOW TO VERIFY THE FILL=X PARAMETER:-',bg='black',fg='white')
label2.pack(fill=X)
label3=Label(root,text='THIS WILL STRETCH THE WINDOW IN VERTICAL DIRECTION',fg='pink', bg='white')
label3.pack(side=LEFT)

frame1=Frame(root)
frame1.pack(side=TOP)
# THIS IS USED TO INITIALISE A FRAME IN TK . AND PLACES IT INSIDE THE WINDOW root.
# THE PACK PARAMETER IS IMP TO PUT IT ON GUI, AT LOCATION SPECIFIED BY SIDE=TOP/BOTTOM/LEFT/RIGHT.


frame1=Frame(root)
frame1.pack(side=BOTTOM)

btn1=Button(frame1,text='BUTTON1',fg='red')
btn2=Button(frame1,text='BUTTON2',fg='black')
btn3=Button(frame1,text='BUTTON3',fg='blue')
btn4=Button(frame1,text='BUTTON4',fg='orange')

# THE BUTTON CLASS INTIALISED THE BUTTON WIDGET AND PLACES IT IN FRAME1/FRAME2 OR ROOT WINDOW.
# THE TEXT PARAMETER WILL BE WHAT WILL BE SHOWN ON TOP OF THE BUTTON.
# FG IS COLOR SHOWN ON TOP OF THE BUTTON
btn1.pack(side=LEFT)
btn2.pack(side=TOP)
btn3.pack(side=RIGHT,ipadx=10)
btn4.pack(side=BOTTOM,ipadx=10)



















