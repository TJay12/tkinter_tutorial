import tkinter as tk
# .pack() = simple vertical/horizontal stacking
# .grid() = table-like row/column layout
# .place() = absolute positioning (x/y)

# <--- pack() --->
layout_pack = tk.Tk()
layout_pack.title("Layout Pack")
layout_pack.geometry("300x200")
# Packs widgets top-to-bottom (or left-to-right).
# Simple, good for quick layouts.
# You can control side, padding, fill, and expand.
label = tk.Label(layout_pack, text="pack")
label.pack(side="top", fill="x",padx=10, pady=5)
button = tk.Button(layout_pack, text="Bpacked")
button.pack(side="bottom", fill="none")

layout_pack.mainloop()

# <--- grid() --->
layout_grid = tk.Tk()
layout_grid.title("Layout Grid")
layout_grid.geometry("300x200")
# Arranges widgets in a grid (rows & columns).
# More control for forms and complex layouts.
# You specify row and column numbers.
label = tk.Label(layout_grid, text="grid")
label.grid(row=0, column=0)
entry = tk.Entry(layout_grid)
entry.grid(row=0, column=1)
button = tk.Button(layout_grid, text="Bgrid")
button.grid(row=1, column=0, columnspan=2)

layout_grid.mainloop()

# <--- place() --->
layout_place = tk.Tk()
layout_place.title("Layout Place")
layout_place.geometry("300x200")
# Precise, absolute positioning with x/y coords.
# Less flexible when resizing windows.
# Useful for very custom layouts.
button = tk.Button(layout_place, text="Bplaced")
button.place(x=50, y=100)

layout_place.mainloop()