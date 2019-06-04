
from tkinter import *
from regionofinterest import regionOfInterest
from resizing import resizingf
from segmentation import segmentationf
from sharpening import sharpeningf
from smoothing import smoothingf
from histogram import histogramf
from webcam_cv3 import liveStreamF
from Capture import capturef
from PIL import Image, ImageTk





root=Tk()

imageFrame=Frame(root)
imageFrame.pack(side=LEFT)


load = Image.open("image.jpg")
render = ImageTk.PhotoImage(load)

img = Label(imageFrame, image=render)
img.image = render
img.place(x=0, y=0)
img.pack()


frameProject=Frame(root)
frameProject.pack(side=TOP)


button_capture=Button(frameProject,text="Capture a Photo",fg="blue",command=capturef,height=5,width=20).grid(row=0,sticky=E)




button_roi=Button(frameProject,text="Region Of Interest",command=regionOfInterest,height=5,width=20).grid(row=1,sticky=E)

button_hist=Button(frameProject,text="Histogram",command=histogramf,height=5,width=20).grid(row=2,sticky=E)

button_resize=Button(frameProject,text="Resizing",command=resizingf,height=5,width=20).grid(row=3,sticky=E)

button_seg=Button(frameProject,text="Segmentation",command=segmentationf,height=5,width=20).grid(row=4,sticky=E)

button_roi=Button(frameProject,text="Sharpening",command=sharpeningf,height=5,width=20).grid(row=5,sticky=E)

button_smooth=Button(frameProject,text="Smoothing",command=smoothingf,height=5,width=20).grid(row=6,sticky=E)

#button_lStream=Button(frameProject,text="Live Stream",command=liveStreamF,height=5,width=20).grid(row=7,sticky=E)

button_lStream=Button(imageFrame,text="Live Stream",command=liveStreamF,height=5,width=30)
button_lStream.pack(side=BOTTOM)



root.mainloop()