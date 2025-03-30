import os
import shutil
import logging
from datetime import datetime

logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def organize_files(source_dir):
    folder_map = {
        'Documents': ['.txt', '.pdf', '.doc', '.docx'],
        'Images': ['.jpg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Source Code': ['.py', '.java', '.cpp'],
        'Archives': ['.zip', '.rar']
    }

    for folder in folder_map.keys():
        if not os.path.exists(os.path.join(source_dir, folder)):
            try:
                os.makedirs(os.path.join(source_dir, folder))
                logging.info(f"Created directory '{folder}'")
            except PermissionError:
                logging.error(f"Permission denied when creating '{folder}'")
                continue

    for filename in os.listdir(source_dir):
        if filename == __file__:
            continue

        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in folder_map.items():
                if file_ext in extensions:
                    try:
                        shutil.move(file_path, os.path.join(source_dir, folder))
                        logging.info(f"Moved '{filename}' to '{folder}'")
                        moved = True
                        break
                    except Exception as e:
                        logging.error(f"Failed to move '{filename}': {str(e)}")
                        break

            if not moved:
                logging.warning(f"No folder found for file '{filename}'")

if __name__ == "__main__":
    source_dir = os.getcwd()
    logging.info("Starting file organization process")
    organize_files(source_dir)
    logging.info("File organization process completed")
    print("File organization completed!")