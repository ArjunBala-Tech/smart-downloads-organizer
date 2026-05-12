# Smart Downloads Organizer

A lightweight, automated Python script that cleans up your cluttered Downloads folder by categorizing files into specific subdirectories based on their extensions. 

I built this project to solve a daily annoyance of losing track of important documents in a sea of installers and random images. It runs locally and requires zero external dependencies.

## Features
* **Cross-Platform:** Automatically detects the correct home directory for both Windows and macOS/Linux.
* **Scalable Dictionary Logic:** Uses a dictionary mapping system rather than nested `if/else` statements, making it simple to add new file types.
* **Crash-Resistant:** Implements `try/except` error handling to gracefully skip files that are currently open or locked by the system, ensuring the script finishes its job.
* **Auto-Directory Generation:** Only creates category folders (like `Images` or `Documents`) if a file of that type is actually detected.

## Built With
* **Python 3.x**
* `os` (Standard Library)
* `shutil` (Standard Library)

##  How to Run It

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/smart-downloads-organizer.git](https://github.com/YOUR_USERNAME/smart-downloads-organizer.git)
