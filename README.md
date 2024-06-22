# Keylogger designed in python
Tested in Windows 10/11
After starting, the keylogger copies the keylogger executable file (if it does not find in the startup programs folder) to the folder C:\Users\<username>\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup user. 
The keylogger saves pressed keys to a text file located in the C:\Users\<username>\AppData\Local\Temp folder. Every 10 seconds the log file is sent to the mega disk.
