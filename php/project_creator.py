import os
import tkinter as tk
from tkinter import filedialog

def create_project_structure(project_name, save_path):
    # Create project directory
    project_dir = os.path.join(save_path, project_name)
    os.makedirs(project_dir)
    os.chdir(project_dir)

    # Create public directory
    public_dir = os.path.join(project_dir, "public")
    os.makedirs(public_dir)

    # Create main PHP file
    main_file_path = os.path.join(public_dir, "index.php")
    with open(main_file_path, "w") as f:
        f.write('<?php\n')
        f.write('// Your PHP code goes here\n')
        f.write('?>\n')

    # Create config directory
    config_dir = os.path.join(project_dir, "config")
    os.makedirs(config_dir)

    # Create database configuration file
    db_config_path = os.path.join(config_dir, "database.php")
    with open(db_config_path, "w") as f:
        f.write('<?php\n')
        f.write('// Your database configuration goes here\n')
        f.write('?>\n')

    print(f"PHP project '{project_name}' created successfully.")

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def create_project():
    project_name = entry_name.get()
    save_path = folder_path.get()
    create_project_structure(project_name, save_path)

# GUI setup
root = tk.Tk()
root.title("PHP Project Creator")

folder_path = tk.StringVar()

label_name = tk.Label(root, text="Project Name:")
label_name.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_path = tk.Label(root, text="Save Path:")
label_path.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry_path = tk.Entry(root, textvariable=folder_path)
entry_path.grid(row=1, column=1, padx=5, pady=5)

button_browse = tk.Button(root, text="Browse", command=browse_button)
button_browse.grid(row=1, column=2, padx=5, pady=5)

button_create = tk.Button(root, text="Create Project", command=create_project)
button_create.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
