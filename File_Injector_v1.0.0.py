import tkinter as tk
from tkinter import filedialog
import shutil
import os

def browse_files():
    filenames = filedialog.askopenfilenames(title="Select file(s) to inject")
    file_list.delete(0, tk.END)
    for file_path in filenames:
        file_list.insert(tk.END, file_path)

def browse_folder():
    folder_path = filedialog.askdirectory(title="Select folder to inject into")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(tk.END, folder_path)

def inject_files():
    files_to_inject = file_list.get(0, tk.END)
    target_folder = folder_entry.get()

    for file_path in files_to_inject:
        try:
            shutil.copy(file_path, target_folder)
            status_label.config(text="Files injected successfully!", fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")
            return

# Create main window
root = tk.Tk()
root.title("File Injector")

# Frame for file selection
file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_label = tk.Label(file_frame, text="Selected Files:")
file_label.grid(row=0, column=0, sticky="w")

file_list = tk.Listbox(file_frame, width=50)
file_list.grid(row=1, column=0, padx=10, pady=5)

file_button = tk.Button(file_frame, text="Browse Files", command=browse_files)
file_button.grid(row=1, column=1, padx=5)

# Frame for folder selection
folder_frame = tk.Frame(root)
folder_frame.pack(pady=10)

folder_label = tk.Label(folder_frame, text="Target Folder:")
folder_label.grid(row=0, column=0, sticky="w")

folder_entry = tk.Entry(folder_frame, width=50)
folder_entry.grid(row=1, column=0, padx=10, pady=5)

folder_button = tk.Button(folder_frame, text="Browse Folder", command=browse_folder)
folder_button.grid(row=1, column=1, padx=5)

# Inject button
inject_button = tk.Button(root, text="Inject Files", command=inject_files)
inject_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
