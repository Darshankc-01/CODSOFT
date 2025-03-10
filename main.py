''' TASK 1 TO-DO LIST A To-Do List application is a useful project
that helps users manage and organize their tasks efficiently.
This project aims to create a command-line or GUI-based application
using Python, allowing users to create, update, and track their to-do lists'''
import tkinter as tk
from tkinter import messagebox, simpledialog
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()
    for task in tasks:
        task_listbox.insert(tk.END, task)
def add_task():
    task = simpledialog.askstring("New Task", "Enter task:")
    if task:
        task_listbox.insert(tk.END, task)
        save_tasks()
def read_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        messagebox.showinfo("Task Details", f"Task: {task}")
    else:
        messagebox.showwarning("Warning", "No task selected.")
def update_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        new_task = simpledialog.askstring("Update Task", "Edit task:", initialvalue=task)
        if new_task:
            task_listbox.delete(selected)
            task_listbox.insert(selected, new_task)
            save_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected.")
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected.")
def browse_tasks():
    tasks = task_listbox.get(0, tk.END)
    messagebox.showinfo("All Tasks", "\n".join(tasks) if tasks else "No tasks available.")
window = tk.Tk()
window.title("TO-DO LIST")
window.geometry("400x400")
frame = tk.Frame(window)
frame.pack(pady=10)
task_listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack()
refresh_task_list()
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
buttons = [
    ("Add", add_task),
    ("Read", read_task),
    ("Update", update_task),
    ("Delete", delete_task),
    ("Browse", browse_tasks)
]
for text, command in buttons:
    tk.Button(button_frame, text=text, width=10, command=command).pack(side=tk.LEFT, padx=5)

window.mainloop()
