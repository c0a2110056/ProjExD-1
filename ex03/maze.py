import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科トン")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    
    tori = tk.PhotoImage(file="fig/5.png")
    cx, cy = 300,400
    canvas.create_image(cx,cy, image=tori,tag=tori)

    root.mainloop()
    