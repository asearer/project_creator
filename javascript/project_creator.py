#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:30:04 2024

@author: asearer
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog

def create_project_structure(project_name, save_directory, project_type):
    # Create main project directory
    project_path = os.path.join(save_directory, project_name)
    os.makedirs(project_path)

    # Create additional directories, subdirectories, and files based on project type
    if project_type == "Basic JavaScript":
        html_dir = os.path.join(project_path, 'html')
        css_dir = os.path.join(project_path, 'css')
        js_dir = os.path.join(project_path, 'js')

        os.makedirs(html_dir)
        os.makedirs(css_dir)
        os.makedirs(js_dir)

        with open(os.path.join(html_dir, 'index.html'), 'w') as html_file:
            html_file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + project_name + '</title>\n</head>\n<body>\n</body>\n</html>')

        with open(os.path.join(css_dir, 'styles.css'), 'w') as css_file:
            css_file.write('/* CSS styles for ' + project_name + ' */')

        with open(os.path.join(js_dir, 'script.js'), 'w') as js_file:
            js_file.write('// JavaScript code for ' + project_name)

    elif project_type == "React":
        src_dir = os.path.join(project_path, 'src')
        os.makedirs(src_dir)

        with open(os.path.join(project_path, 'package.json'), 'w') as package_file:
            package_file.write('{ "name": "' + project_name + '", "version": "1.0.0", "private": true }')

        with open(os.path.join(src_dir, 'App.js'), 'w') as app_file:
            app_file.write('import React from "react";\n\nfunction App() {\n  return (\n    <div>\n      <h1>' + project_name + '</h1>\n    </div>\n  );\n}\n\nexport default App;')

    elif project_type == "Vue.js":
        with open(os.path.join(project_path, 'index.html'), 'w') as html_file:
            html_file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + project_name + '</title>\n<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>\n</head>\n<body>\n</body>\n</html>')

        with open(os.path.join(project_path, 'app.js'), 'w') as js_file:
            js_file.write('// Vue.js code for ' + project_name)

    elif project_type == "Angular":
        src_dir = os.path.join(project_path, 'src')
        os.makedirs(src_dir)

        with open(os.path.join(src_dir, 'app.component.ts'), 'w') as ts_file:
            ts_file.write('// Angular component code for ' + project_name)

    elif project_type == "Three.js":
        js_dir = os.path.join(project_path, 'js')
        os.makedirs(js_dir)

        with open(os.path.join(project_path, 'index.html'), 'w') as html_file:
            html_file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + project_name + '</title>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n</head>\n<body>\n</body>\n</html>')

        with open(os.path.join(js_dir, 'script.js'), 'w') as js_file:
            js_file.write('// Three.js code for ' + project_name)

    elif project_type == "Node.js":
        src_dir = os.path.join(project_path, 'src')
        os.makedirs(src_dir)

        with open(os.path.join(project_path, 'package.json'), 'w') as package_file:
            package_file.write('{\n  "name": "' + project_name + '",\n  "version": "1.0.0",\n  "description": "",\n  "main": "src/index.js",\n  "scripts": {\n    "start": "node src/index.js"\n  },\n  "keywords": [],\n  "author": "",\n  "license": "ISC"\n}')

        with open(os.path.join(src_dir, 'index.js'), 'w') as js_file:
            js_file.write('// Node.js code for ' + project_name)

    result_label.config(text=f'{project_type} project structure created for {project_name}.')

def select_directory():
    selected_directory = filedialog.askdirectory()
    save_directory_entry.delete(0, tk.END)
    save_directory_entry.insert(0, selected_directory)

def on_submit():
    project_name = project_name_entry.get()
    save_directory = save_directory_entry.get()
    project_type = project_type_combo.get()
    
    create_project_structure(project_name, save_directory, project_type)

root = tk.Tk()
root.title("Project Structure Creator")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

project_name_label = ttk.Label(mainframe, text="Project Name:")
project_name_label.grid(column=0, row=0, sticky=tk.W)

project_name_entry = ttk.Entry(mainframe)
project_name_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

save_directory_label = ttk.Label(mainframe, text="Save Directory:")
save_directory_label.grid(column=0, row=1, sticky=tk.W)

save_directory_entry = ttk.Entry(mainframe)
save_directory_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

select_directory_button = ttk.Button(mainframe, text="Select Directory", command=select_directory)
select_directory_button.grid(column=2, row=1)

project_type_label = ttk.Label(mainframe, text="Project Type:")
project_type_label.grid(column=0, row=2, sticky=tk.W)

project_type = tk.StringVar()
project_type_combo = ttk.Combobox(mainframe, textvariable=project_type, values=["Basic JavaScript", "React", "Vue.js", "Angular", "Three.js", "Node.js"])
project_type_combo.grid(column=1, row=2, sticky=(tk.W, tk.E))

submit_button = ttk.Button(mainframe, text="Create Project", command=on_submit)
submit_button.grid(column=0, row=3, columnspan=3)

result_label = ttk.Label(mainframe, text="")
result_label.grid(column=0, row=4, columnspan=3)

root.mainloop()
