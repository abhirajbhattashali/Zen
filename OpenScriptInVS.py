import os
import time
import subprocess

def create_program_file(filename, content):
    # Create the file with the given filename
    with open(filename, 'w') as file:
        file.write(content)

    # Open the file in VS Code
    subprocess.run(['open', '-a', 'Visual Studio Code', filename])
    time.sleep(3)

    # Use AppleScript to switch back to the previous application 3
    subprocess.run([
        'osascript', '-e',
        'tell application "System Events" to keystroke tab using command down'
    ])

if __name__ == "__main__":
    # Input: Source code content and filename
    source_code = input("Enter the source code:\n")
    file_name = input("Enter the file name (with extension, e.g., 'program.py'):\n")

    # Create file and open it in VS Code
    create_program_file(file_name, source_code)
