import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Image and File Viewer")
root.geometry("700x500")

# Create canvas
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=10)

# Create label
label = tk.Label(root, text="Open an image or text file")
label.pack()

# Open image or text file
def open_file(event=None):
    filename = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not filename:
        return

    try:
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img = Image.open(filename)
            img.thumbnail((500, 300))

            photo = ImageTk.PhotoImage(img)
            canvas.delete("all")
            canvas.create_image(250, 150, image=photo)
            canvas.image = photo

            label.config(text="Image: " + filename)

        elif filename.lower().endswith(".txt"):
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            canvas.delete("all")
            canvas.create_text(
                10, 10,
                anchor="nw",
                text=content,
                width=480,
                fill="black"
            )

            label.config(text="Text File: " + filename)

        else:
            messagebox.showwarning(
                "Unsupported File",
                "Please select an image or text file."
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Change background color
def change_color():
    color = colorchooser.askcolor(title="Choose Background Color")

    if color[1]:
        canvas.config(bg=color[1])


# Show information
def show_info():
    messagebox.showinfo(
        "Information",
        "Interactive Image and File Viewer\n"
        "Open images or text files and change the background color."
    )


# Buttons
tk.Button(root, text="Open File", command=open_file).pack(pady=5)
tk.Button(root, text="Change Background", command=change_color).pack(pady=5)
tk.Button(root, text="About", command=show_info).pack(pady=5)

# Bind keyboard and mouse events
root.bind("<Return>", open_file)
canvas.bind("<Button-1>", lambda event: change_color())

# Run application
root.mainloop()