from PIL import Image, ImageFilter

# Open image
img = Image.open("image.jpg")

# Display menu
print("1. Grayscale")
print("2. Black and White")
print("3. Blur")

choice = input("Enter your choice: ")

# Apply filter
if choice == "1":
    result = img.convert("L")
    print("Grayscale image created.")

elif choice == "2":
    img = img.convert("L")
    result = img.point(lambda x: 255 if x > 128 else 0)
    print("Black and White image created.")

elif choice == "3":
    result = img.filter(ImageFilter.BLUR)
    print("Blur image created.")

else:
    print("Invalid choice")
    exit()

# Save output image
result.save("output.png")
print("Image saved as output.png")