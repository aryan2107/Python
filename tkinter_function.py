
from tkinter import *

root=Tk()
def printName():
    x=input('PRESS ENTER YOUR NAME:-')
    print('YOUR NAME IS {0}'.format(x))

# THE BELOW WIDGET IS BOUND TO THE FUNCTION printName.
# THE BUTTTON CLICK WILL CALL THE FUCTION AND WILL EXECUTE IT
btn1=Button(root,text='ENTER UR NAME',command=printName)
btn1.pack()
