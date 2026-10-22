
import tkinter as tk
import math

def calculate_area():
    radius = float(entry.get())
    area = math.pi * radius * radius
    result.config(text="Area of Circle = " + str(round(area, 2)))

root = tk.Tk()
root.title("Area of Circle")

tk.Label(root, text="Enter Radius").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate Area", command=calculate_area).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
