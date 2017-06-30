'''
from tkinter import *

root=Tk()
def printName():
    x=input('PRESS ENTER YOUR NAME:-')
    print('YOUR NAME IS {0}'.format(x))

# THE BELOW WIDGET IS BOUND TO THE FUNCTION printName.
# THE BUTTTON CLICK WILL CALL THE FUCTION AND WILL EXECUTE IT
btn1=Button(root,text='ENTER UR NAME',command=printName)
btn1.pack()
'''

######## OR #################

# THE EVENT IS PASSED TO THE FUNCTION. THE EVENT CAN BE LEFT-CLICK, RIGHT-CLICK
# KEYBOARD PRESS ETC.
# <Button-1> is left-click.
from tkinter import *

root=Tk()
def printName(event):
    x=input('PRESS ENTER YOUR NAME:-')
    print('YOUR NAME IS {0}'.format(x))

btn1=Button(root,text='ENTER UR NAME')
btn1.bind('<Button-1>',printName)
btn1.pack()
