from tkinter import *
def ShowText():
    labelText.set(entry.get())
def ShowValue():
    print(radibuttonvariable.get())
root = Tk()
radibuttonvariable =StringVar()
label =Label(root,text="which name you love most..!!")
label.pack()
Radiobutton(root,text = "PAVI",value='PAVI',variable=radibuttonvariable).pack()
Radiobutton(root,text="PALLAVI",value='PALLAVI',variable=radibuttonvariable).pack()
Radiobutton(root,text = "BUJJI",value='BUJJI',variable=radibuttonvariable).pack()
Button(root,text="showvalue",command=ShowValue).pack()
entry =Entry(root,bg='red',fg='white')
entry.pack()

Button(root,text="Show text",command =ShowText).pack()
labelText = StringVar()
labelText.set("------")
label =Label(root,textvariable = labelText)
label.pack()
root.mainloop()
