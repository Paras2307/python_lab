import tkinter as tk
from tkinter import filedialog, messagebox

# Main window
root = tk.Tk()
root.title("Student Record Manager")
root.geometry("500x600")

# Variables
gender = tk.StringVar(value="Male")
sports = tk.IntVar()

# Student name
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Roll number
tk.Label(root, text="Roll Number:").pack()
roll_entry = tk.Entry(root, width=40)
roll_entry.pack()

# Course
tk.Label(root, text="Course:").pack()
course_entry = tk.Entry(root, width=40)
course_entry.pack()

# Gender selection
tk.Label(root, text="Gender:").pack()
tk.Radiobutton(root, text="Male", variable=gender, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender, value="Female").pack()

# Sports selection
tk.Checkbutton(
    root, text="Interested in Sports", variable=sports
).pack()

# Address
tk.Label(root, text="Address:").pack()
address_text = tk.Text(root, width=40, height=4)
address_text.pack()

# Save student record
def save_record():
    name = name_entry.get()
    roll = roll_entry.get()
    course = course_entry.get()
    address = address_text.get("1.0", tk.END).strip()

    if not name or not roll or not course:
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    record = (
        f"Name: {name}\n"
        f"Roll Number: {roll}\n"
        f"Course: {course}\n"
        f"Gender: {gender.get()}\n"
        f"Sports: {'Yes' if sports.get() else 'No'}\n"
        f"Address: {address}\n"
        f"{'-' * 30}\n"
    )

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        with open(filename, "a") as file:
            file.write(record)

        messagebox.showinfo("Success", "Record saved successfully!")


# View student records
def view_records():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        try:
            with open(filename, "r") as file:
                data = file.read()

            # Display records in a new window
            window = tk.Toplevel(root)
            window.title("Student Records")

            text = tk.Text(window, width=60, height=25)
            text.pack()
            text.insert(tk.END, data)

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Clear form
def clear_form():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    gender.set("Male")
    sports.set(0)


# Delete saved file
def delete_records():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this file?"
        )

        if confirm:
            import os
            try:
                os.remove(filename)
                messagebox.showinfo("Success", "File deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))


# Buttons
tk.Button(root, text="Save Record", command=save_record).pack(pady=5)
tk.Button(root, text="View Records", command=view_records).pack(pady=5)
tk.Button(root, text="Delete Record File", command=delete_records).pack(pady=5)
tk.Button(root, text="Clear Form", command=clear_form).pack(pady=5)

# Run application
root.mainloop()