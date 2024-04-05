import os
import tkinter as tk
from tkinter import filedialog

def create_project_structure(project_name, package_name, save_path):
    # Create project directory
    project_dir = os.path.join(save_path, project_name)
    os.makedirs(project_dir)
    os.chdir(project_dir)

    # Create source directory
    src_dir = os.path.join(project_dir, "src")
    os.makedirs(src_dir)

    # Create package directory
    package_dir = os.path.join(src_dir, package_name.replace('.', '/'))
    os.makedirs(package_dir)

    # Create main class file
    main_class_path = os.path.join(package_dir, f"{project_name}.java")
    with open(main_class_path, "w") as f:
        f.write(f'package {package_name};\n\n')
        f.write(f'public class {project_name} ' + '{\n')
        f.write('    public static void main(String[] args) {\n')
        f.write('        // Your main Java code goes here\n')
        f.write('    }\n')
        f.write('}\n')

    print(f"Java project '{project_name}' created successfully.")

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def create_project():
    project_name = entry_name.get()
    package_name = entry_package.get()
    save_path = folder_path.get()
    create_project_structure(project_name, package_name, save_path)

# GUI setup
root = tk.Tk()
root.title("Java Project Creator")

folder_path = tk.StringVar()

label_name = tk.Label(root, text="Project Name:")
label_name.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_package = tk.Label(root, text="Package Name:")
label_package.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry_package = tk.Entry(root)
entry_package.grid(row=1, column=1, padx=5, pady=5)

label_path = tk.Label(root, text="Save Path:")
label_path.grid(row=2, column=0, sticky="w", padx=5, pady=5)

entry_path = tk.Entry(root, textvariable=folder_path)
entry_path.grid(row=2, column=1, padx=5, pady=5)

button_browse = tk.Button(root, text="Browse", command=browse_button)
button_browse.grid(row=2, column=2, padx=5, pady=5)

button_create = tk.Button(root, text="Create Project", command=create_project)
button_create.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
