import os
import sys

# 1. Show current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# 2. List files and folders
print("\nFiles and Folders:")
for item in os.listdir(current_dir):
    print(item)

# 3. Create a workspace folder
workspace = os.path.join(current_dir, "workspace")

if not os.path.exists(workspace):
    os.mkdir(workspace)
    print("\nWorkspace folder created.")
else:
    print("\nWorkspace folder already exists.")

# 4. Navigate to workspace
os.chdir(workspace)
print("Current Directory after navigation:", os.getcwd())

# 5. List only .txt files
print("\nText Files:")
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)

# 6. Get filename from command-line argument
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "log.txt"

# 7. Create/read the log file safely using context manager
file_path = os.path.join(workspace, filename)

try:
    # Create file if it does not exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("Log file created successfully.\n")
        print("\nNew log file created:", filename)

    # Read the file
    with open(file_path, "r") as file:
        content = file.read()

    print("\nLog File Content:")
    print(content)

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Error:", e)

# 8. Show final directory
print("\nFinal Directory:", os.getcwd())