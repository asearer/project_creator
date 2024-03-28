#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 06:59:42 2024

@author: asearer
"""

import os
import tkinter as tk
from tkinter import messagebox, filedialog

def create_chatbot_project(project_path, project_name):
    # Define directory structure
    project_dir = os.path.join(project_path, project_name)
    directories = [
        os.path.join(project_dir, 'data'),
        os.path.join(project_dir, 'src'),
        os.path.join(project_dir, 'src/intents'),
        os.path.join(project_dir, 'src/actions'),
        os.path.join(project_dir, 'src/utils')
    ]

    # Create project directory
    os.makedirs(project_dir)
    os.chdir(project_dir)

    # Create directories
    for directory in directories:
        os.makedirs(directory)

    # Create files and write boilerplate code
    with open(os.path.join(project_dir, 'src/main.py'), 'w') as file:
        file.write("# Main file for running the chatbot\n")
        file.write("from intents import intents\n")
        file.write("from actions import actions\n")
        file.write("from chatbot import Chatbot\n\n")
        file.write("# Initialize Chatbot\n")
        file.write("chatbot = Chatbot(intents=intents, actions=actions)\n\n")
        file.write("# Start the chatbot\n")
        file.write("chatbot.start()\n")

    with open(os.path.join(project_dir, 'src/intents/__init__.py'), 'w'):
        pass

    with open(os.path.join(project_dir, 'src/actions/__init__.py'), 'w'):
        pass

    with open(os.path.join(project_dir, 'src/utils/__init__.py'), 'w'):
        pass

    with open(os.path.join(project_dir, 'chatbot.py'), 'w') as file:
        file.write("# Chatbot class definition\n")
        file.write("class Chatbot:\n")
        file.write("    def __init__(self, intents, actions):\n")
        file.write("        self.intents = intents\n")
        file.write("        self.actions = actions\n")
        file.write("    \n")
        file.write("    def start(self):\n")
        file.write("        print('Chatbot started!')\n")

    messagebox.showinfo("Success", f"Chatbot project '{project_name}' created successfully.")

def create_project():
    project_path = filedialog.askdirectory()
    if project_path:
        project_name = entry.get()
        if project_name:
            create_chatbot_project(project_path, project_name)
            root.destroy()
        else:
            messagebox.showwarning("Warning", "Please enter a project name.")

# GUI setup
root = tk.Tk()
root.title("Chatbot Project Creator")

label_dir = tk.Label(root, text="Select directory to create project:")
label_dir.pack(pady=5)

button_browse = tk.Button(root, text="Browse", command=create_project)
button_browse.pack(pady=5)

label_name = tk.Label(root, text="Enter project name:")
label_name.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

root.mainloop()
