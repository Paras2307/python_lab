import tkinter as tk

# Create window
root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("300x400")

# Display
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button function
def click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    elif value == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, value)

# Calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0

for b in buttons:
    tk.Button(
        root, text=b, width=5, height=2,
        font=("Arial", 14),
        command=lambda x=b: click(x)
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1

# Run calculator
root.mainloop()