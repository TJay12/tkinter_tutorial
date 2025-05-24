import tkinter as tk

# <--- Add Button Functionality --->
def on_click():
    user_text = entry.get()
    # This reads whatever the user typed into it.
    print("You typed:",user_text)

def on_click2():
    user_text = entry.get()
    # entry.get() pulls the text the user typed.
    label.config(text=f"You said: {user_text}")
    # label.config(text=...) changes what the label says dynamically

# <--- Create a basic window --->
# Create the main window
root = tk.Tk()
root.title("Interactive App")
root.geometry("300x200") # Width x Height

# <--- Add some widgets --->
# Label
label = tk.Label(root, text="Type Something:")
label.pack(pady=(20,0))
# Entry field
entry = tk.Entry(root)
# You can type into the entry field.
entry.pack()
# Button 1
button = tk.Button(root, text="Print", command=on_click)
# Click the button
# Your input will print to the console (or terminal)
button.pack(pady=(10, 0), padx=10)
# Button 2
button = tk.Button(root, text="Submit", command=on_click2)
# Click the button

button.pack(pady=(10, 0), padx=10)

# <--- Exit Button --->
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10, padx=10)

# <----- Start the GUI event loop ----->
root.mainloop()
