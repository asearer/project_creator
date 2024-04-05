import os
import tkinter as tk
from tkinter import filedialog

def create_project_structure(project_name, save_path):
    # Create project directory
    project_dir = os.path.join(save_path, project_name)
    os.makedirs(project_dir)
    os.chdir(project_dir)

    # Create directories for source code and tests
    os.makedirs("src")
    os.makedirs("tests")

    # Create main script file
    with open(f"src/{project_name}.js", "w") as f:
        f.write('// Your main Node.js code goes here\n')

    # Create test script file
    with open(f"tests/test_{project_name}.js", "w") as f:
        f.write('// Your tests go here\n')

    # Create package.json file
    with open("package.json", "w") as f:
        f.write('{\n')
        f.write(f'  "name": "{project_name}",\n')
        f.write('  "version": "1.0.0",\n')
        f.write('  "description": "",\n')
        f.write('  "main": "src/index.js",\n')
        f.write('  "scripts": {\n')
        f.write('    "test": "echo \\"Error: no test specified\\" && exit 1"\n')
        f.write('  },\n')
        f.write('  "keywords": [],\n')
        f.write('  "author": "",\n')
        f.write('  "license": "ISC"\n')
        f.write('}\n')

    print(f"Project '{project_name}' created successfully.")

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
root.title("Node.js Project Creator")

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
