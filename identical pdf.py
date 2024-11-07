import hashlib
import tkinter as tk
from tkinter import messagebox

def hash_file(fileName1, fileName2): 
    h1 = hashlib.sha1() 
    h2 = hashlib.sha1() 

    # Read and hash the first file
    with open(fileName1, "rb") as file: 
        chunk = 0
        while chunk != b'': 
            chunk = file.read(1024) 
            h1.update(chunk) 

    # Read and hash the second file
    with open(fileName2, "rb") as file: 
        chunk = 0
        while chunk != b'': 
            chunk = file.read(1024) 
            h2.update(chunk) 

    return h1.hexdigest(), h2.hexdigest() 

def compare_files():
    file1 = file1_entry.get()
    file2 = file2_entry.get()

    try:
        msg1, msg2 = hash_file(file1, file2) 

        if msg1 != msg2: 
            result = "These files are not identical"
        else: 
            result = "These files are identical"
    except FileNotFoundError:
        result = "One or both files not found. Please check the file names."
    except Exception as e:
        result = f"An error occurred: {str(e)}"

    # Display the result in a message box
    messagebox.showinfo("Comparison Result", result)

# Create the main window
root = tk.Tk()
root.title("PDF File Comparison")
root.geometry("400x200")

# Create labels and entries for file input
file1_label = tk.Label(root, text="Enter first PDF file name:")
file1_label.pack(pady=10)
file1_entry = tk.Entry(root, width=50)
file1_entry.pack(pady=5)

file2_label = tk.Label(root, text="Enter second PDF file name:")
file2_label.pack(pady=10)
file2_entry = tk.Entry(root, width=50)
file2_entry.pack(pady=5)

# Create a button to compare files
compare_button = tk.Button(root, text="Compare Files", command=compare_files)
compare_button.pack(pady=20)

# Start the application
root.mainloop()
