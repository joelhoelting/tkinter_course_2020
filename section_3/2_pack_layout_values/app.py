import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle1", bg="green", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_2 = tk.Label(root, text="Rectangle2", bg="blue", fg="white")
rectangle_2.pack(side="top", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_3 = tk.Label(root, text="Rectangle3", bg="black", fg="white")
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

root.mainloop()
