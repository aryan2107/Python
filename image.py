from tkinter import *
root=Tk()
#root.geometry('1048x768')

# THE BELOW METHOD ONLY USES GIF FILES AND NOT JPEG.
# FOR JPEG FILES U NEED TO USE PIL MODULE. DOWNLOAD , IMPORT AND USE IT.
photo=PhotoImage(file='C:\\ClickHeartGIF.gif')
label=Label(root,image=photo)

label.pack()
root.mainloop()
