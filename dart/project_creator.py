# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:56:32 2024

@author: asearer
"""

import os
import tkinter as tk
from tkinter import messagebox

def create_project():
    project_name = project_name_entry.get()
    if not project_name:
        messagebox.showerror("Error", "Please enter a project name.")
        return

    # Create project directory
    project_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Create lib directory
    lib_dir = os.path.join(project_dir, "lib")
    os.makedirs(lib_dir, exist_ok=True)

    # Create main Dart file
    main_file = os.path.join(lib_dir, project_name + ".dart")
    with open(main_file, "w") as f:
        f.write('void main() {\n  print("Hello, ' + project_name + '!");\n}')

    messagebox.showinfo("Success", f"Project '{project_name}' created successfully.")
    root.destroy()

root = tk.Tk()
root.title("Dart Project Creator")

project_name_label = tk.Label(root, text="Project Name:")
project_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

project_name_entry = tk.Entry(root)
project_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

create_button = tk.Button(root, text="Create Project", command=create_project)
create_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
