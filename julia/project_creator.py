# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:17:08 2024

@author: asearer
"""

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def create_project():
    project_name = project_name_entry.get()
    if not project_name:
        messagebox.showerror("Error", "Please enter a project name.")
        return

    save_location = filedialog.askdirectory(title="Select save location")
    if not save_location:
        messagebox.showerror("Error", "Please select a save location.")
        return

    # Create project directory
    project_dir = os.path.join(save_location, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Create src directory
    src_dir = os.path.join(project_dir, "src")
    os.makedirs(src_dir, exist_ok=True)

    # Create main Julia file
    main_file = os.path.join(src_dir, project_name + ".jl")
    with open(main_file, "w") as f:
        f.write(f'# Main file for {project_name}\n\n')

    # Create test Julia file
    test_dir = os.path.join(project_dir, "test")
    os.makedirs(test_dir, exist_ok=True)
    test_file = os.path.join(test_dir, "test_" + project_name + ".jl")
    with open(test_file, "w") as f:
        f.write(f'# Test file for {project_name}\n\n')

    messagebox.showinfo("Success", f"Project '{project_name}' created successfully.")
    root.destroy()

root = tk.Tk()
root.title("Julia Project Creator")

project_name_label = tk.Label(root, text="Project Name:")
project_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

project_name_entry = tk.Entry(root)
project_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

create_button = tk.Button(root, text="Create Project", command=create_project)
create_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
