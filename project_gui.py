from tkinter import *


root=Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame =Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text="STREAM",fg="red")
button2=Button(topFrame,text="RESIZE",fg="blue")
button3=Button(topFrame,text="BINARIZATION",fg="red")
button4=Button(bottomFrame,text="SCALING",fg="red")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
"""

label1=Label(root,text="Name")
label2=Label(root,text="Password")

entry1=Entry(root)
entry2=Entry(root)

label1.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c=Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)
"""




root.mainloop()