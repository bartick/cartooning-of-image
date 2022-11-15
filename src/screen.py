from tkinter import filedialog, Tk, Frame, TOP, Label, Button, BOTTOM
from PIL import ImageTk,Image
import os
from typing import Optional

class Screen:
    def __init__(self, root: Tk, width: int, height: int, title: Optional[str]="Screen", icon: Optional[str]="", resizable: Optional[bool]=True) -> None:
        self.root = root
        self.width = width
        self.height = height
        self.resizable = resizable
        self.title = title
        self.icon = icon

    def create(self) -> None:
        self.root.title(self.title)
        self.root.iconbitmap(self.icon)
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(self.resizable, self.resizable)

        self.labelFrame = Frame(self.root, width=self.width, height=self.height)
        self.labelFrame.pack(side=TOP)

        self.frame = Frame(self.root, width=self.width, height=self.height)
        self.frame.pack(side=BOTTOM, padx=10, pady=10)

        self.label = Label(self.labelFrame)
        self.label.pack(side=TOP, padx=10, pady=10)

        self.browseButton = Button(self.frame, text="Browse", command=self.browse)
        self.browseButton.pack(side="left")

        self.convertButton = Button(self.frame, text="Convert", command=self.convert)
        self.convertButton.pack(side="left", padx=5)

        self.saveButton = Button(self.frame, text="Save", command=self.save)
        self.saveButton.pack(side="left", padx=5)
    
    def browse(self) -> None:
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG FIle", "*.jpg"),("PNG File", "*.png"),("ALL Files","*.*")))
        self.image = Image.open(fln)
        self.imageSize = self.image.size
        imageResizer = (self.width if self.width < self.imageSize[0] else self.imageSize[0], self.imageSize[1] if self.imageSize[1] < self.height-70 else self.height-70)
        self.image = self.image.resize(imageResizer, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.label.configure(image=self.image)
        self.label.image=self.image
    
    def convert(self) -> None:
        self.image = self.image.convert("L")
        self.image = ImageTk.PhotoImage(self.image)
        self.label.config(image=self.image)
        self.label.image = self.image
    
    def save(self) -> None:
        self.filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save as", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))
        imageToSave: Image = ImageTk.getimage(self.image)
        imageToSave.resize(self.imageSize, Image.ANTIALIAS).save(self.filename)
    
    @property
    def run(self) -> None:
        self.root.mainloop()