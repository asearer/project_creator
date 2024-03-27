#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:49:15 2024

@author: asearer
"""

import os
import tkinter as tk
from tkinter import messagebox, filedialog

def create_flask_project(project_name, directory):
    # Create project directory
    project_path = os.path.join(directory, project_name)
    os.makedirs(project_path)
    
    # Create Flask app file
    with open(f"{project_path}/app.py", "w") as file:
        file.write(f"from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run(debug=True)")

    messagebox.showinfo("Success", f"Flask project '{project_name}' created successfully!")

def create_django_project(project_name, directory):
    # Create Django project directory
    project_path = os.path.join(directory, project_name)
    os.makedirs(project_path)
    
    # Create Django project
    os.system(f"django-admin startproject {project_name} --directory {project_path}")
    
    # Create app directory and __init__.py file
    app_path = os.path.join(project_path, project_name)
    os.makedirs(app_path)
    with open(os.path.join(app_path, "__init__.py"), "w") as file:
        pass
    
    # Create views.py file with default view
    with open(os.path.join(app_path, "views.py"), "w") as file:
        file.write("from django.http import HttpResponse\n\n")
        file.write("def index(request):\n")
        file.write("    return HttpResponse('Hello, Django!')")

    messagebox.showinfo("Success", f"Django project '{project_name}' created successfully!")

def create_projects():
    project_name = project_name_entry.get()
    if not project_name:
        messagebox.showerror("Error", "Please enter a project name.")
        return

    project_type = project_type_var.get()
    if project_type == "Flask":
        create_flask_project(project_name, directory_var.get())
    elif project_type == "Django":
        create_django_project(project_name, directory_var.get())

# Create GUI
root = tk.Tk()
root.title("Project Creator")

project_name_label = tk.Label(root, text="Project Name:")
project_name_label.pack()
project_name_entry = tk.Entry(root)
project_name_entry.pack()

project_type_label = tk.Label(root, text="Select Project Type:")
project_type_label.pack()
project_type_var = tk.StringVar(root)
project_type_var.set("Flask")
project_type_menu = tk.OptionMenu(root, project_type_var, "Flask", "Django")
project_type_menu.pack()

directory_label = tk.Label(root, text="Select Directory:")
directory_label.pack()
directory_var = tk.StringVar(root)
directory_var.set(os.getcwd())  # Default directory is current working directory
directory_entry = tk.Entry(root, textvariable=directory_var)
directory_entry.pack()

def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_var.set(directory)

choose_directory_button = tk.Button(root, text="Browse", command=choose_directory)
choose_directory_button.pack()

create_button = tk.Button(root, text="Create Projects", command=create_projects)
create_button.pack()

root.mainloop()
