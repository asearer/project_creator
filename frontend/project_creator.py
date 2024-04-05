#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 05:20:54 2024

@author: asearer
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import os
import subprocess
import re
import string

class BoilerplateGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Boilerplate Code Generator")

        # Dropdown to select frontend language/framework
        self.language_label = ttk.Label(master, text="Select Frontend Language/Framework:")
        self.language_label.pack()
        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(master, textvariable=self.language_var)
        self.language_dropdown['values'] = ('HTML', 'CSS', 'JavaScript', 'React')
        self.language_dropdown.pack()

        # Button to generate boilerplate code
        self.generate_button = ttk.Button(master, text="Generate Code", command=self.generate_code)
        self.generate_button.pack()

    def generate_code(self):
        selected_language = self.language_var.get()

        # Generating boilerplate code based on selected language/framework
        if selected_language == 'HTML':
            self.generate_html()
        elif selected_language == 'CSS':
            self.generate_css()
        elif selected_language == 'JavaScript':
            self.generate_javascript()
        elif selected_language == 'React':
            self.generate_react()

    def generate_html(self):
        default_name = "html_project"
        project_name = filedialog.asksaveasfilename(defaultextension="", initialfile=default_name)
        if not project_name:
            return

        # Create project directory
        os.makedirs(project_name)
        os.chdir(project_name)

        # Create index.html
        with open("index.html", "w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n</head>\n<body>\n  <script src='script.js'></script>\n</body>\n</html>")

        messagebox.showinfo("Success", f"HTML project '{project_name}' created successfully!")

    def generate_css(self):
        default_name = "css_project"
        project_name = filedialog.asksaveasfilename(defaultextension="", initialfile=default_name)
        if not project_name:
            return

        # Create project directory
        os.makedirs(project_name)
        os.chdir(project_name)

        # Create styles.css
        with open("styles.css", "w") as f:
            f.write("/* CSS */\n\nbody {\n  /* Styles */\n}")

        messagebox.showinfo("Success", f"CSS project '{project_name}' created successfully!")

    def generate_javascript(self):
        default_name = "javascript_project"
        project_name = filedialog.asksaveasfilename(defaultextension="", initialfile=default_name)
        if not project_name:
            return

        # Create project directory
        os.makedirs(project_name)
        os.chdir(project_name)

        # Create script.js
        with open("script.js", "w") as f:
            f.write("// JavaScript\n\nconsole.log('Hello, World!');")

        messagebox.showinfo("Success", f"JavaScript project '{project_name}' created successfully!")

    def generate_react(self):
        default_name = "react_project"
        project_name = filedialog.asksaveasfilename(defaultextension="", initialfile=default_name)
        if not project_name:
            return

        # Create React project using create-react-app
        os.system(f"npx create-react-app {project_name}")
        messagebox.showinfo("Success", f"React project '{project_name}' created successfully!")

def main():
    root = tk.Tk()
    app = BoilerplateGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
