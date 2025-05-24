import tkinter as tk
# .pack() = simple vertical/horizontal stacking
# .grid() = table-like row/column layout
# .place() = absolute positioning (x/y)

root = tk.Tk()
root.title("Layout")
root.geometry("300x200")

label = tk.Label(root, text="Type Here")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

button = tk.Button(root, text="Button")
button.grid(row=1, column=0, columnspan=2)





root.mainloop()
