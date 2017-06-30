from tkinter import *
root=Tk()

frame2=Frame(root)
frame2.pack()
v=StringVar()

label1=Label(frame2,text='Name')
entry1=Entry(frame2,textvariable=v)
label1.pack()
entry1.pack()

label2=Label(frame2,text='Password')
label2.pack()
entry2=Entry(frame2)
entry2.pack()

s=entry2.get()

label3=Label(root,text=s,bg='blue')
label3.pack(fill=X)



chk=Checkbutton(frame2,text='KEEP ME LOGGED IN')
chk.pack()

btn=Button(frame2,text='SUBMIT')
btn.pack()


if s=='aryan':
    print ('WORKED')

#root.mainloop()
