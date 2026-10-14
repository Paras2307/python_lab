import tkinter as tk
from tkinter import messagebox
import json

# Main application
root = tk.Tk()
root.title("Multi-Frame Dashboard")
root.geometry("600x400")

# Application data
config = {"username": "", "theme": "light"}

# Menu bar
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Save Configuration", command=lambda: save_config())
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Dashboard frame
dashboard_frame = tk.Frame(main_frame)
dashboard_frame.pack(fill="both", expand=True)

tk.Label(
    dashboard_frame,
    text="Welcome to Dashboard",
    font=("Arial", 20)
).pack(pady=20)

# Username input
tk.Label(dashboard_frame, text="Enter Username:").pack()

username_entry = tk.Entry(dashboard_frame)
username_entry.pack(pady=5)

# Status label
status_label = tk.Label(dashboard_frame, text="Ready")
status_label.pack(pady=10)


# Show dashboard information
def show_dashboard():
    name = username_entry.get()

    if name.strip():
        config["username"] = name
        status_label.config(text="Welcome, " + name)
    else:
        messagebox.showwarning("Warning", "Please enter a username!")


# Save configuration to file
def save_config():
    config["username"] = username_entry.get()

    try:
        with open("dashboard_config.json", "w") as file:
            json.dump(config, file, indent=4)

        messagebox.showinfo("Success", "Configuration saved successfully!")

    except OSError as e:
        messagebox.showerror("Error", str(e))


# Settings frame
settings_frame = tk.Frame(main_frame)

tk.Label(
    settings_frame,
    text="Dashboard Settings",
    font=("Arial", 18)
).pack(pady=20)

tk.Label(settings_frame, text="Select Theme:").pack()

theme_var = tk.StringVar(value="light")

tk.Radiobutton(
    settings_frame, text="Light",
    variable=theme_var, value="light"
).pack()

tk.Radiobutton(
    settings_frame, text="Dark",
    variable=theme_var, value="dark"
).pack()


def save_theme():
    config["theme"] = theme_var.get()
    save_config()


tk.Button(
    settings_frame,
    text="Save Theme",
    command=save_theme
).pack(pady=10)


# Frame navigation
def show_frame(frame):
    dashboard_frame.pack_forget()
    settings_frame.pack_forget()
    frame.pack(fill="both", expand=True)


# Navigation buttons
tk.Button(
    dashboard_frame,
    text="Open Settings",
    command=lambda: show_frame(settings_frame)
).pack(pady=5)

tk.Button(
    settings_frame,
    text="Back to Dashboard",
    command=lambda: show_frame(dashboard_frame)
).pack(pady=5)

# Display dashboard initially
show_frame(dashboard_frame)

# Run application
root.mainloop()