import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("300x400")

# Display field
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button click function
def click(value):
    entry.insert(tk.END, value)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Clear display
def clear():
    entry.delete(0, tk.END)

# Calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        command = calculate
    else:
        command = lambda value=text: click(value)

    tk.Button(
        root, text=text, width=5, height=2,
        command=command, font=("Arial", 14)
    ).grid(row=row, column=col, padx=3, pady=3)

# Clear button
tk.Button(
    root, text="Clear", width=25, command=clear
).grid(row=5, column=0, columnspan=4, pady=10)

# Run application
root.mainloop()