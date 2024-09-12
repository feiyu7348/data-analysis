from tkinter import *
from tkinter import Tk
root = Tk()
root.title("myTitle")
label1 = Label(root,text='first Number')
label1.grid(row = 0,column=0)
text1 = Text(root,width=30,height=1)
text1.grid(row=1,column=0)

label2 = Label(root,text='Second Number')
label2.grid(row = 2,column=0)
text2 = Text(root,width=30,height=1)
text2.grid(row=4,column=0)
text3 = Text(root,width=30,height=1)
text3.grid(row=5,column=0)

def myCalculate():
    a1 = int(text1.get("1.0",END))
    a2 = int(text2.get("1.0", END))
    a3 = a1+a2
    text3.delete('1.0',END)
    text3.insert(INSERT,a3)

button1 = Button(root,text="click for sum",command=myCalculate)
button1.grid(row=6,column=0)

mainloop()

