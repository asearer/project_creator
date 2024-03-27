#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:16:10 2024

@author: asearer
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog

def create_ml_project_structure():
    project_name = project_name_entry.get().strip()
    project_type = project_type_combobox.get().lower()
    project_path = project_path_entry.get().strip()

    if not project_name:
        result_label.config(text="Please enter a project name.")
        return

    if not project_path:
        result_label.config(text="Please select a project path.")
        return

    if not os.path.isdir(project_path):
        result_label.config(text="Invalid project path.")
        return

    # Create project directory if it doesn't exist
    project_dir = os.path.join(project_path, project_name)
    os.makedirs(project_dir, exist_ok=True)

    if project_type == 'classification':
        create_classification_boilerplate(project_dir)
    elif project_type == 'regression':
        create_regression_boilerplate(project_dir)
    elif project_type == 'clustering':
        create_clustering_boilerplate(project_dir)
    else:
        result_label.config(text="Invalid project type.")
        return

    result_label.config(text=f"Created directory structure and boilerplate code for '{project_name}'.")

def choose_directory():
    directory = filedialog.askdirectory()
    project_path_entry.delete(0, tk.END)
    project_path_entry.insert(0, directory)

def create_classification_boilerplate(project_dir):
    # Create subdirectories if they don't exist
    for directory in ['data', 'models', 'notebooks', 'src', 'reports', 'docs']:
        dir_path = os.path.join(project_dir, directory)
        os.makedirs(dir_path, exist_ok=True)

    # Create README.md
    with open(os.path.join(project_dir, 'README.md'), 'w') as readme:
        readme.write("# Classification Project\n\nThis project contains code and resources for a classification machine learning project.")

    # Create requirements.txt
    with open(os.path.join(project_dir, 'requirements.txt'), 'w') as requirements:
        requirements.write("numpy\npandas\nscikit-learn")

    # Create main.py
    with open(os.path.join(project_dir, 'src', 'main.py'), 'w') as main_file:
        main_file.write("# Main script for classification project")

def create_regression_boilerplate(project_dir):
    # Create subdirectories if they don't exist
    for directory in ['data', 'models', 'notebooks', 'src', 'reports', 'docs']:
        dir_path = os.path.join(project_dir, directory)
        os.makedirs(dir_path, exist_ok=True)

    # Create README.md
    with open(os.path.join(project_dir, 'README.md'), 'w') as readme:
        readme.write("# Regression Project\n\nThis project contains code and resources for a regression machine learning project.")

    # Create requirements.txt
    with open(os.path.join(project_dir, 'requirements.txt'), 'w') as requirements:
        requirements.write("numpy\npandas\nscikit-learn")

    # Create main.py
    with open(os.path.join(project_dir, 'src', 'main.py'), 'w') as main_file:
        main_file.write("# Main script for regression project")

def create_clustering_boilerplate(project_dir):
    # Create subdirectories if they don't exist
    for directory in ['data', 'models', 'notebooks', 'src', 'reports', 'docs']:
        dir_path = os.path.join(project_dir, directory)
        os.makedirs(dir_path, exist_ok=True)

    # Create README.md
    with open(os.path.join(project_dir, 'README.md'), 'w') as readme:
        readme.write("# Clustering Project\n\nThis project contains code and resources for a clustering machine learning project.")

    # Create requirements.txt
    with open(os.path.join(project_dir, 'requirements.txt'), 'w') as requirements:
        requirements.write("numpy\npandas\nscikit-learn")

    # Create main.py
    with open(os.path.join(project_dir, 'src', 'main.py'), 'w') as main_file:
        main_file.write("# Main script for clustering project")

# Create GUI
root = tk.Tk()
root.title("ML Project Structure Creator")

# Project Name
project_name_label = ttk.Label(root, text="Enter project name:")
project_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
project_name_entry = ttk.Entry(root)
project_name_entry.grid(row=0, column=1, padx=5, pady=5)

# Project Path
project_path_label = ttk.Label(root, text="Select project path:")
project_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
project_path_entry = ttk.Entry(root)
project_path_entry.grid(row=1, column=1, padx=5, pady=5)
project_path_button = ttk.Button(root, text="Browse", command=choose_directory)
project_path_button.grid(row=1, column=2, padx=5, pady=5)

# Project Type
project_type_label = ttk.Label(root, text="Select project type:")
project_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
project_type_combobox = ttk.Combobox(root, values=["Classification", "Regression", "Clustering"])
project_type_combobox.grid(row=2, column=1, padx=5, pady=5)
project_type_combobox.current(0)

# Create Button
create_button = ttk.Button(root, text="Create Project", command=create_ml_project_structure)
create_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Result Label
result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
