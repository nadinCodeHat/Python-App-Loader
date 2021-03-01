import tkinter as tk
from tkinter import filedialog as fd, Text
import os

window = tk.Tk()
window.title("Python App Loader")

canvas = tk.Canvas(window,width=700,height=700,bg='lightgray')
canvas.pack()


frame = tk.Frame(window, bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

openfileBtn = tk.Button(window,text="Open File",fg="black",pady=10,padx=10)
openfileBtn.pack()

runBtn = tk.Button(window,text="Run",fg="black",pady=10,padx=25)
runBtn.pack()

window.mainloop()