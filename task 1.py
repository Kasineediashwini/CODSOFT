import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if confirmed:
        task_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Task entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Task list
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear All", width=10, command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
