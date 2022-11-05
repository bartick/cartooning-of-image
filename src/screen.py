from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import filedialog
import tkinter as tk

def showimage():
    fln=filedialog.askopenfilename(initialdir = os.getcwd(),title="Select Image File",filetypes=(("JPG FIle", "*.jpg"),("PNG File", "*.png"),("ALL Files","*.*")))
    img = Image.open(fln)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img
def convert():
    return True
def save():
    return True
root=Tk()



frn=Frame(root)
frn.pack(side=BOTTOM,padx=15,pady=15)

lbl=Label(root)
lbl.pack()

btn=Button(frn,text="Browse Image",command=showimage)
btn.pack(side=tk.LEFT)

btn3=Button(frn,text="Save", command=save)
btn3.pack(side=tk.LEFT,padx=5)

btn2=Button(frn,text="Convert",command=convert)
btn2.pack(side=tk.LEFT,padx =10)





root.title("CARTOONING OF IMAGE")
root.geometry("800x700")
root.mainloop()