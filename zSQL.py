# too Lazy to create files and folder manually...smh :p

import os

# Take folder name input
folder_name = input("Enter the folder name: ")

# Create the folder
os.makedirs(folder_name, exist_ok=True)
print(f"Folder '{folder_name}' created successfully.\n")

# Files to create
files = ["psql.py", "pandas.py.java", "README.md"]

# Function to take multiline input
def get_multiline_input(file_name):
    print(f"Enter the content for '{file_name}'. Type 'EOF' on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        lines.append(line)
    return "\n".join(lines)

# Create files and write content
for file_name in files:
    file_path = os.path.join(folder_name, file_name)
    content = get_multiline_input(file_name)
    with open(file_path, "w", encoding="utf-8") as f:  # <- specify UTF-8
        f.write(content)
    print(f"Content written to '{file_path}'\n")

print("All files created successfully!")
