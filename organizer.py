import os
import shutil

# 1. Define our categories using a dictionary. 
# This makes it super easy to add new file types later without changing the core logic.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".heic"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Installers": [".exe", ".dmg", ".pkg", ".msi"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Media": [".mp4", ".mp3", ".wav", ".mkv", ".mov"]
}

def organize_folder(folder_path):
    """Sorts files in the specified folder into categorized subfolders."""
    
    # 2. Safety check: Does the directory actually exist?
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    print(f"Scanning '{folder_path}' for unorganized files...\n")
    moved_count = 0

    # 3. Loop through every item in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's already a folder (we only want to move files)
        if os.path.isdir(file_path):
            continue

        # Extract the file extension (e.g., '.jpg') and make it lowercase
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # 4. Determine which category folder it belongs to
        target_folder_name = "Others" # Default fallback for unknown file types
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                target_folder_name = category
                break

        # Create the category folder if it doesn't exist yet
        target_folder_path = os.path.join(folder_path, target_folder_name)
        if not os.path.exists(target_folder_path):
            os.makedirs(target_folder_path)

        # 5. Move the file with error handling (try/except)
        try:
            shutil.move(file_path, os.path.join(target_folder_path, filename))
            print(f"Moved: {filename}  -->  [{target_folder_name}]")
            moved_count += 1
        except Exception as e:
            print(f"Skipped {filename} (File might be open or in use). Error: {e}")

    print(f"\nSuccess! Cleaned up {moved_count} files.")

if __name__ == "__main__":
    # Automatically finds the Downloads folder for both Windows and Mac/Linux users
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    
    organize_folder(downloads_dir)