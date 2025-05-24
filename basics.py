import tkinter as tk
# This brings in the Tkinter library and lets you use its features with tk, like; tk.Tk(), tk.Label(), etc.

# <--- Create a basic window --->
# Create the main window
root = tk.Tk()
# This creates the main window for your app.
# It’s your "root" container. Everything goes inside this

# Set a title
root.title("My First Tkinter App")
# Gives your window a title (shows in the title bar at the top).
# Set a window size
root.geometry("300x200") # Width x Height
# Optional, but handy. Sets the window size in pixels: width x height.

# <--- Add some widgets --->
# Label
label = tk.Label(root, text="Hello, Tkinter!")
# tk.Label(root, ...) creates a label inside the root window.
# text="Hello" is the message it shows.
label.pack()
# .pack() tells it to show up, without a layout method like pack(), widgets won’t be visible.

# Entry field
entry = tk.Entry(root)
# tk.Entry(...) creates a single-line text box.
# root is the parent (the main window).
entry.pack()
# .pack() makes it appear on the screen.

# Button
button = tk.Button(root, text="click me")
# tk.Button(...) creates a clickable button.
# text="Click Me" sets the label on the button.
button.pack(pady=(10,0), padx=10)
# .pack() again makes it appear.

# <--- Exit Button --->
exit_button = tk.Button(root, text="Exit", command=root.quit)
# command=some_function tells the button what to do when clicked.
#   This must be a function without parentheses (e.g. on_click, not on_click()).
exit_button.pack(pady=10, padx=10)
# .pack() again makes it appear.

# <----- Start the GUI event loop ----->
root.mainloop()
# Starts the Tkinter event loop. Without this, the window opens and closes immediately.
#     This loop waits for events like button clicks, typing, etc., and keeps the app running.