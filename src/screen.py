from tkinter import filedialog, Tk, Frame, TOP, Label, Button, BOTTOM
from PIL import ImageTk,Image
import os
from typing import Optional
import cv2
from numpy import uint8
from sklearn.cluster import KMeans

class Screen:
    def __init__(self, root: Tk, width: int, height: int, title: Optional[str]="Screen", icon: Optional[str]="", resizable: Optional[bool]=True) -> None:
        """
            Screen class for creating a screen for the application to convert image to cartoon.
        """
        self.root = root
        self.width = width
        self.height = height
        self.resizable = resizable
        self.title = title
        self.icon = icon

    def create(self) -> None:
        """
            Create the screen for the application.
            This method creates the screen for the application and sets proper buttons and labels.
        """
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
        self.browseButton.pack(side="left", padx=10)

        self.convertButton = Button(self.frame, text="Convert", command=self.convert)
        self.convertButton.pack(side="left", padx=10)

        self.saveButton = Button(self.frame, text="Save", command=self.save)
        self.saveButton.pack(side="left", padx=10)
    
    def browse(self) -> None:
        """
            Browse for the image to convert to cartoon.
        """
        self.imageFile = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG FIle", "*.jpg"),("PNG File", "*.png"), ("JPEG File", "*.jpeg"),("ALL Files","*.*")))
        self.image = Image.open(self.imageFile)
        self.imageSize = self.image.size
        self.imageResizer = (self.width if self.width < self.imageSize[0] else self.imageSize[0], self.imageSize[1] if self.imageSize[1] < self.height-70 else self.height-70)
        self.image = self.image.resize(self.imageResizer, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.label.configure(image=self.image)
        self.label.image=self.image
    
    def convert(self) -> None:
        """
            Convert the image to cartoon.
        """
        img = cv2.imread(self.imageFile)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        line_size = 7
        blur_value = 7
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray_blur = cv2.medianBlur(gray_img, blur_value)
        edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)

        k = 7
        data = img.reshape(-1, 3)
        kmeans = KMeans(n_clusters=k, random_state=42).fit(data)
        img_reduced = kmeans.cluster_centers_[kmeans.labels_]
        img_reduced = img_reduced.reshape(img.shape)
        img_reduced = img_reduced.astype(uint8)

        blurred = cv2.bilateralFilter(img_reduced, d=7, sigmaColor=200,sigmaSpace=200)
        cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

        # cartoon_ = cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR)

        self.image = Image.fromarray(cartoon)
        self.image = self.image.resize(self.imageResizer, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.label.configure(image=self.image)
        self.label.image=self.image
    
    def save(self) -> None:
        """
            Save the image to the desired location.
        """
        self.filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save as", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))
        imageToSave: Image = ImageTk.getimage(self.image)
        imageToSave.resize(self.imageSize, Image.ANTIALIAS).save(self.filename)
    
    @property
    def run(self) -> None:
        self.root.mainloop()