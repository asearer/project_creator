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
        self.language_dropdown['values'] = ('HTML', 'CSS', 'JavaScript', 'React', 'Angular', 'Vue.js')
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
        elif selected_language == 'Angular':
            self.generate_angular()
        elif selected_language == 'Vue.js':
            self.generate_vue()

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

    def generate_angular(self):
        default_name = "angular_project"
        project_name = filedialog.asksaveasfilename(defaultextension="", initialfile=default_name)
        if not project_name:
            return

        # Create Angular project using Angular CLI
        os.system(f"ng new {project_name} --style=css --routing --skip-tests")
        messagebox.showinfo("Success", f"Angular project '{project_name}' created successfully!")

    def generate_vue(self):
        # Ask user for directory to save the project
        project_dir = filedialog.askdirectory()
        if not project_dir:
            return

        # Use the default project name for Vue.js projects
        project_name = "vue"

        if not self.check_vue_cli():
            self.install_vue_cli()

        # Select preset
        preset = simpledialog.askstring("Preset Selection", "Please pick a preset: (Use arrow keys)",
                                        initialvalue="Default (Vue 3)")

        if preset:
            # Create Vue.js project using Vue CLI with selected preset
            project_path = os.path.join(project_dir, self.convert_to_url_friendly(project_name))
            os.system(f'vue create --preset="{preset}" {project_path}')
            messagebox.showinfo("Success", f"Vue.js project '{project_path}' created successfully!")
        else:
            messagebox.showinfo("Info", "No preset selected. Defaulting to Vue 3 preset.")

            # Create Vue.js project using Vue CLI with default preset (Vue 3)
            project_path = os.path.join(project_dir, self.convert_to_url_friendly(project_name))
            os.system(f'vue create --preset="Default (Vue 3)" {project_path}')
            messagebox.showinfo("Success", f"Vue.js project '{project_path}' created successfully!")

    def check_vue_cli(self):
        try:
            subprocess.run(['vue', '--version'], capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def install_vue_cli(self):
        messagebox.showinfo("Vue CLI Not Found", "Vue CLI is not installed. Installing Vue CLI...")

        try:
            subprocess.run(['npm', 'install', '-g', '@vue/cli'], check=True)
            messagebox.showinfo("Success", "Vue CLI installed successfully!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Vue CLI. Please install it manually.")

    def convert_to_url_friendly(self, name):
        valid_chars = string.ascii_letters + string.digits + '-_'
        return ''.join(c if c in valid_chars else '-' for c in name)

def main():
    root = tk.Tk()
    app = BoilerplateGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
