import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

def generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        messagebox.showinfo("Generated Password", f"Your password is:\n{password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for the length")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label_length = tk.Label(root, text="Enter desired password length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack()

# Run the main event loop
root.mainloop()
