import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk

# Create window
root = tk.Tk()
root.title("Image and File Viewer")
root.geometry("600x500")

# Label
label = tk.Label(root, text="Image and File Viewer",
                 font=("Arial", 16))
label.pack(pady=10)

# Display area
display = tk.Label(root, text="Open an image or text file")
display.pack(pady=20)

# Open image
def open_image():
    file = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if file:
        try:
            img = Image.open(file)
            img.thumbnail((400, 300))
            photo = ImageTk.PhotoImage(img)

            display.config(image=photo, text="")
            display.image = photo

        except Exception as e:
            messagebox.showerror("Error", str(e))

# Open text file
def open_text():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        try:
            with open(file, "r") as f:
                content = f.read()

            display.config(image="", text=content,
                           wraplength=500, justify="left")
            display.image = None

        except Exception as e:
            messagebox.showerror("Error", str(e))

# Change background color
def change_color():
    color = colorchooser.askcolor()[1]

    if color:
        root.config(bg=color)
        label.config(bg=color)

# Buttons
tk.Button(root, text="Open Image",
          command=open_image).pack(pady=5)

tk.Button(root, text="Open Text File",
          command=open_text).pack(pady=5)

tk.Button(root, text="Change Background Color",
          command=change_color).pack(pady=5)

# Keyboard event
root.bind("<Return>", lambda event: open_image())

# Run application
root.mainloop()