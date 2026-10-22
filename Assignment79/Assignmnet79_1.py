
import tkinter as tk

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.config(text="Sum = " + str(num1 + num2))

root = tk.Tk()
root.title("Addition of Two Numbers")

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
