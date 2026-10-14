import traceback

# Custom exception
class InvalidFileFormat(Exception):
    pass


# File processing function
def process_file(filename):
    file = None

    try:
        file = open(filename, "r")

        data = file.read()

        if not data.strip():
            raise InvalidFileFormat("File is empty!")

        print("File content:")
        print(data)

    except FileNotFoundError:
        print("Error: File not found!")

    except InvalidFileFormat as e:
        print("Error:", e)
        traceback.print_exc()

    except Exception:
        print("An unexpected error occurred!")
        traceback.print_exc()

    else:
        print("File processed successfully!")

    finally:
        if file is not None:
            file.close()
        print("File closed safely.")


# Main program
filename = input("Enter file name: ")
process_file(filename)