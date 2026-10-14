import tkinter as tk
from tkinter import messagebox
import json

# Create main window
root = tk.Tk()
root.title("Dashboard Application")
root.geometry("500x400")

# Application data
data = {"username": "", "theme": "Light"}

# Save configuration
def save_data():
    with open("config.json", "w") as file:
        json.dump(data, file)
    messagebox.showinfo("Success", "Configuration saved")

# Show home frame
def show_home():
    settings_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)

# Show settings frame
def show_settings():
    home_frame.pack_forget()
    settings_frame.pack(fill="both", expand=True)

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

menu.add_command(label="Home", command=show_home)
menu.add_command(label="Settings", command=show_settings)
menu.add_command(label="Save", command=save_data)

# Home frame
home_frame = tk.Frame(root)
tk.Label(home_frame, text="Welcome to Dashboard",
         font=("Arial", 18)).pack(pady=20)

tk.Button(home_frame, text="Open Settings",
          command=show_settings).pack()

# Settings frame
settings_frame = tk.Frame(root)

tk.Label(settings_frame, text="Settings",
         font=("Arial", 18)).pack(pady=10)

tk.Label(settings_frame, text="Enter Username").pack()

username = tk.Entry(settings_frame)
username.pack()

theme = tk.StringVar(value="Light")

tk.Radiobutton(settings_frame, text="Light",
               variable=theme, value="Light").pack()

tk.Radiobutton(settings_frame, text="Dark",
               variable=theme, value="Dark").pack()

def update_data():
    data["username"] = username.get()
    data["theme"] = theme.get()
    messagebox.showinfo("Success", "Settings updated")

tk.Button(settings_frame, text="Update Settings",
          command=update_data).pack(pady=10)

tk.Button(settings_frame, text="Back Home",
          command=show_home).pack()

# Show home initially
home_frame.pack(fill="both", expand=True)

# Run application
root.mainloop()