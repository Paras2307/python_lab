import traceback

# Custom exception
class InvalidFileError(Exception):
    pass

try:
    file = open("data.txt", "r")

    for line in file:
        if not line.strip():
            raise InvalidFileError("Empty line found")
        print(line.strip())

except FileNotFoundError:
    print("Error: File not found")

except InvalidFileError as e:
    print("Error:", e)
    traceback.print_exc()

except Exception as e:
    print("Unexpected error:", e)

else:
    print("File processed successfully")

finally:
    try:
        file.close()
        print("File closed")
    except NameError:
        print("File was not opened")
