




Open the terminal in Visual Studio Code and run the following command to compile the Python code into an executable file:
pyinstaller --onefile main.py

This will create an executable file called "dist/main.exe". You can run this file to start monitoring the specified folder.


The code will create a file called "folder_monitor.log" in the current directory and write a note to the file when a file or folder is changed.
