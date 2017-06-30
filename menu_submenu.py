
from tkinter import *

def donothing():
    print('ITS WORKING')
    
root=Tk()

# MENU IS ANOTHER WIDGET CREATING CLASS LIKE BUTTON, CHECKBUTTON, ENTRY, LABEL
# IT SHOULD BE CALLED UPON THE PARENT WINDOW WHICH IS ROOT

m=Menu(root)
root.config(menu=m)

# SUBMENU WILL BE NEEDED FOR EVERY MENU ITEM LIKE FILE, EDIT, FORMAT, RUN.
# THEY ALL HAVE SUBMENU'S INSIDE THEM
# MENU WILL CONSISTS OF FILE, EDIT, FORMAT, RUN items. MENU NEEDS TO BE CASCADED TO
# FORM SUBMENU. EVERY SUBMENU WILL HAVE LABELS LIKE NEW FILE, OPEN, CUT , COPY ,PASTE.
# THERE WILL BE A COMMAND/ACTION WHEN YOU CLICK ON ANY OF THE SUBMENU'S. LIKE
# OPEN SHOULD OPEN A NEW FILE. THATS TAKEN CARE BY COMMAND PARAMETER.

submenu=Menu(m)
m.add_cascade(label='File',menu=submenu)
submenu.add_command(label='New File',command=donothing)
submenu.add_command(label='Open',command=donothing)
submenu.add_command(label='Recent Files', command=donothing)
submenu.add_command(label='Save', command=donothing)
submenu.add_separator()
# SEPARATOR IS A LINE WHICH SEPARATES TWO SECTION'S OF SUBMENU.
submenu.add_command(label='Close', command=donothing)
submenu.add_command(label='Exit', command=donothing)



editMenu=Menu(m)
m.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=donothing)
editMenu.add_command(label='Redo' , command=donothing)
editMenu.add_separator()

formatMenu=Menu(m)
m.add_cascade(label='Format', menu=formatMenu)
formatMenu.add_command(label='Indent', command=donothing)
formatMenu.add_separator()
formatMenu.add_command(label='Cut', command=donothing)
formatMenu.add_command(label='Copy', command=donothing)
formatMenu.add_command(label='Paste', command=donothing)


