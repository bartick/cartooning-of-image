from src import Screen
from tkinter import Tk

if __name__ == "__main__":
    screen = Screen(
        root=Tk(),
        width=1000,
        height=750,
        title="CARTOONING OF IMAGE",
        resizable=True,
    )
    screen.create()
    screen.run