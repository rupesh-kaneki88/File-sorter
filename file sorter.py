#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import re
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def sort_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Regular expression pattern to match file extensions
    pattern = r'\.([a-zA-Z0-9]+)$'

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Check if the path is a file
        if os.path.isfile(source_path):
            # Use regular expression to extract the file extension
            match = re.search(pattern, filename)
            if match:
                # Extract the extension from the matched object
                extension = match.group(1)
                # Create a destination directory based on the extension
                destination_subdir = os.path.join(destination_dir, extension)

                # Create the destination directory if it doesn't exist
                if not os.path.exists(destination_subdir):
                    os.makedirs(destination_subdir)

                # Move the file to the destination directory
                destination_path = os.path.join(destination_subdir, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {destination_path}")

def select_source_directory():
    directory = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, directory)

def select_destination_directory():
    directory = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, directory)

def sort_button_clicked():
    source_dir = source_entry.get()
    destination_dir = destination_entry.get()
    sort_files(source_dir, destination_dir)
    tk.messagebox.showinfo("File Sorting", "Sorting completed!")

# Create the main window
window = tk.Tk()
window.title("File Sorting Program")
window.geometry('400x400')

# Create source directory selection
source_label = tk.Label(window, text="Source Directory:")
source_label.pack()
source_entry = tk.Entry(window)
source_entry.pack()
source_button = tk.Button(window, text="Browse", command=select_source_directory)
source_button.pack()

# Create destination directory selection
destination_label = tk.Label(window, text="Destination Directory:")
destination_label.pack()
destination_entry = tk.Entry(window)
destination_entry.pack()
destination_button = tk.Button(window, text="Browse", command=select_destination_directory)
destination_button.pack()

# Create sort button
sort_button = tk.Button(window, text="Sort Files", command=sort_button_clicked)
sort_button.pack()

# Start the main event loop
window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




