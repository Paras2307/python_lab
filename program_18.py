import tkinter as tk
from tkinter import messagebox, filedialog
import json

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("400x500")

students = {}

# Student details
tk.Label(root, text="Student Record Manager",
         font=("Arial", 16)).pack()

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Roll Number").pack()
roll = tk.Entry(root)
roll.pack()

tk.Label(root, text="Course").pack()
course = tk.Entry(root)
course.pack()

# Gender selection
tk.Label(root, text="Gender").pack()
gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").pack()

# Checkbutton
sports = tk.IntVar()
tk.Checkbutton(root, text="Interested in Sports",
               variable=sports).pack()

# Address
tk.Label(root, text="Address").pack()
address = tk.Text(root, height=3, width=30)
address.pack()

# Save record
def save_record():
    r = roll.get()

    if not name.get() or not r or not course.get():
        messagebox.showerror("Error", "Fill all fields")
        return

    students[r] = {
        "Name": name.get(),
        "Course": course.get(),
        "Gender": gender.get(),
        "Sports": sports.get(),
        "Address": address.get("1.0", tk.END).strip()
    }

    file = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json")]
    )

    if file:
        with open(file, "w") as f:
            json.dump(students, f, indent=4)
        messagebox.showinfo("Success", "Record saved")

# Retrieve record
def retrieve_record():
    file = filedialog.askopenfilename(
        filetypes=[("JSON Files", "*.json")]
    )

    if file:
        with open(file, "r") as f:
            data = json.load(f)

        students.update(data)
        r = roll.get()

        if r in students:
            s = students[r]
            name.delete(0, tk.END)
            name.insert(0, s["Name"])
            course.delete(0, tk.END)
            course.insert(0, s["Course"])
            gender.set(s["Gender"])
            sports.set(s["Sports"])
            address.delete("1.0", tk.END)
            address.insert("1.0", s["Address"])
        else:
            messagebox.showerror("Error", "Record not found")

# Delete record
def delete_record():
    r = roll.get()

    if r in students:
        del students[r]
        messagebox.showinfo("Success", "Record deleted")
    else:
        messagebox.showerror("Error", "Record not found")

# Buttons
tk.Button(root, text="Save Record",
          command=save_record).pack(pady=5)

tk.Button(root, text="Retrieve Record",
          command=retrieve_record).pack(pady=5)

tk.Button(root, text="Delete Record",
          command=delete_record).pack(pady=5)

root.mainloop()