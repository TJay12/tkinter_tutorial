import tkinter as tk

main = tk.Tk()
main.title("Grid Layout")
main.geometry("200x400")

# <--- Even Column Weighting --->
# When using .grid(), Tkinter doesn't auto-resize columns evenly unless you tell it to.
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)
main.grid_columnconfigure(2, weight=1)
# This tells each of the 3 columns to expand evenly, which fixes the alignment and balances any remaining space.
# <--- Even Row Weighting --->
main.grid_rowconfigure(0, weight=1)
main.grid_rowconfigure(1, weight=1)
main.grid_rowconfigure(2, weight=1)
main.grid_rowconfigure(3, weight=1)
main.grid_rowconfigure(4, weight=1)

# <--- Lable --->
title = tk.Label(main, text="Even Grid")
title.grid(row=0, columnspan=3, ipadx=10, ipady=10)

# <--- Buttons --->
one = tk.Button(main, text="1")
one.grid(row=1, column=0, ipadx=10, ipady=5)
two = tk.Button(main, text="2")
two.grid(row=1, column=1, ipadx=10, ipady=5)
three = tk.Button(main, text="3")
three.grid(row=1, column=2, ipadx=10, ipady=5)
four = tk.Button(main, text="4")
four.grid(row=2, column=0, ipadx=10, ipady=5)
five = tk.Button(main, text="5")
five.grid(row=2, column=1, ipadx=10, ipady=5)
six = tk.Button(main, text="6")
six.grid(row=2, column=2, ipadx=10, ipady=5)
seven = tk.Button(main, text="7")
seven.grid(row=3, column=0, ipadx=10, ipady=5)
eight = tk.Button(main, text="8")
eight.grid(row=3, column=1, ipadx=10, ipady=5)
nine = tk.Button(main, text="9")
nine.grid(row=3, column=2, ipadx=10, ipady=5)
zero = tk.Button(main, text="0")
zero.grid(row=4, column=1, ipadx=10, ipady=5)

# <--- Center Entire Window on Screen --->
# Place this after you've added and placed all your widgets.
main.update_idletasks()
width = main.winfo_width()
height = main.winfo_height()
x = (main.winfo_screenwidth() // 2) - (width // 2)
y = (main.winfo_screenheight() // 2) - (height // 2)
main.geometry(f"{width}x{height}+{x}+{y}")

# <--- !Main Loop! --->
main.mainloop()