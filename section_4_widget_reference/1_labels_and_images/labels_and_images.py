import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Widget Examples")
root.geometry("600x400")
root.resizable(False, False)

image = Image.open("github.png").resize((64, 64))
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root, text="image with text", image=photo, padding=5, compound="right")
label.pack()

# greeting = tk.StringVar()
# label = ttk.Label(root, padding=10, textvariable=greeting)
# label.pack()
#
# greeting.set("Hello, John")

root.mainloop()
