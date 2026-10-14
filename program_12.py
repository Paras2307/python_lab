from PIL import Image, ImageFilter

# Open image
path = input("Enter image path: ")
img = Image.open(path).convert("RGB")

print("1. Grayscale")
print("2. Black and White")
print("3. Blur")
print("4. Save Original Copy")

choice = int(input("Enter your choice: "))

if choice == 1:
    # Convert image to grayscale
    result = img.convert("L")
    print("Image converted to grayscale.")

elif choice == 2:
    # Convert image to black and white
    gray = img.convert("L")
    result = gray.point(lambda x: 255 if x > 128 else 0)
    print("Image converted to black and white.")

elif choice == 3:
    # Apply blur filter
    result = img.filter(ImageFilter.BLUR)
    print("Blur filter applied.")

elif choice == 4:
    # Keep original image unchanged
    result = img

else:
    print("Invalid choice.")
    exit()

# Save processed image
output_path = input("Enter output file name (e.g., output.png): ")
result.save(output_path)

print("Image saved successfully as", output_path)