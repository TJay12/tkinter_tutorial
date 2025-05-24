import tkinter as tk
# For more advanced font management, Tkinter provides the tkinter.font module,
# allowing you to create and reuse named fonts across widgets.
import tkinter.font as tkFont

root = tk.Tk()
root.title("Styling")
root.geometry("300x200")

# You can customize the font of widgets using the font parameter
label = tk.Label(root, text="Styled Text", font=("Helvetica", 16, "bold italic"))
# Font Family: "Helvetica", "Arial", "Times New Roman", etc.
# Size: An integer value, e.g., 16.
# Style: "bold", "italic", "underline", or combinations like "bold italic".
label.pack(pady=(20,0))

# Customize text and background colors using the fg and bg parameters
label2 = tk.Label(root,text="Colored Text", fg="blue", bg="yellow")
label2.pack(pady=(20,0))
# You can use standard color names like "red", "green", "blue",
# or hexadecimal color codes like "#FF5733".

# For more control, especially when reusing font styles,
# utilize the tkinter.font module
custom_font = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic")
label3 = tk.Label(root, text="Custom Font", font=custom_font)
label3.pack(pady=(20,0))

root.mainloop()