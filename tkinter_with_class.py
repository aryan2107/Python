

from tkinter import *

class MyWidget():
# MASTER IS NOTHING BUT THE ROOT WINDOW PASSED. USE ONLY MASTER TO ACCESS ROOT.
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        # command parameter is used to bind the function to the event.
        # HERE WHEN SUBMIT IS CLICKED, IT CALLS self.printMsg Function
        self.btn1=Button(frame,text='SUBMIT',command=self.printMsg)
        # frame.quit is an inbuilt tkinter function that closes the frame when
        # button QUIT is clicked
        self.btn2=Button(frame,text='QUIT',command=frame.quit)
        self.btn1.pack(side=LEFT)
        self.btn2.pack(side=LEFT)

    def printMsg(self):
        print('ITS WORKING')


root=Tk()
obj=MyWidget(root)
root.mainloop()
