from tkinter import *

def ChangeToRed():
    labelText.set("Colour changed")
    label.config(bg = 'red')
def ChangeToGreen():
    labelText.set("Colour changed")
    label.config(bg = 'green')
def ChangeToBlue():
    labelText.set("Colour changed")
    label.config(bg = 'blue')
root = Tk()
Label(root,text="which is your fav???").pack()

Checkbutton(root,text="check1").pack()
Checkbutton(root,text="check2").pack()
Checkbutton(root,text="check3").pack()



labelText = StringVar()
labelText.set("first label")
label = Label(root, textvariable =labelText)
label.pack()

Button(root,text="RED",command = ChangeToRed).pack()
Button(root,text="Green",command=ChangeToGreen).pack()
Button(root,text="Blue",command=ChangeToBlue).pack()
root.mainloop()
