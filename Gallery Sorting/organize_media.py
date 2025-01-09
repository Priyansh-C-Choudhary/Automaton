import os
import shutil
from datetime import datetime
from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path

# Source directory where the photos and videos are stored
source_dir = ""

# Destination directory to organize files
destination_dir = ""

# Create destination directory if it doesn't exist
Path(destination_dir).mkdir(parents=True, exist_ok=True)

# Supported file extensions
photo_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".heic", ".heif"}
video_extensions = {".mp4", ".avi", ".mov", ".mkv"}

# Register HEIC/HEIF opener
register_heif_opener()

# Function to get the creation date
def get_file_date(file_path):
    try:
        # Try reading EXIF data for photos
        if Path(file_path).suffix.lower() in photo_extensions:
            with Image.open(file_path) as img:
                exif_data = img._getexif()
                if exif_data and 36867 in exif_data:
                    return datetime.strptime(exif_data[36867], "%Y:%m:%d %H:%M:%S")
        # Fall back to file creation time
        return datetime.fromtimestamp(os.path.getmtime(file_path))
    except Exception as e:
        print(f"Error reading date for {file_path}: {e}")
        return None

# Process files in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        ext = Path(file).suffix.lower()

        # Check if the file is a photo or video
        if ext in photo_extensions or ext in video_extensions:
            date = get_file_date(file_path)
            if date:
                # Create year/month folder
                year_month_folder = date.strftime("%Y-%m")
                target_folder = os.path.join(destination_dir, year_month_folder)
                Path(target_folder).mkdir(parents=True, exist_ok=True)

                # Move the file
                try:
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved: {file} -> {target_folder}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")
            else:
                print(f"Could not determine date for: {file}")
