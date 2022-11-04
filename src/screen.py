import tkinter

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

    def draw(self, x, y, color):
        self.canvas.create_rectangle(x, y, x+100, y+100, fill=color)
        self.canvas.update()

    def mainloop(self):
        self.root.mainloop()