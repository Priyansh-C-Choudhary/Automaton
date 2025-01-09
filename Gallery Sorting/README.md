# Photo and Video Organizer 📂✨

A super chill script to organize your messy photos and videos into year/month folders based on their creation date. No more endless scrolling through unorganized files. Let this script do the boring work for you!

## 🛠️ Setup Instructions

1. **Clone or download the script.**
2. **Install the required dependencies:**
   Run the following command to install `Pillow` and `pillow-heif`:
   ```bash
   pip install pillow pillow-heif
   ```
3. Set up your source and destination directories: Edit these lines in the script to match your folder structure:
  ```
  source_dir = ""  # Change this to your source folder
  destination_dir = ""  # Change this to your destination folder
  ```
  Example: 
  ```
  Example: destination_dir = "D:/My Adventures/Trial/Organized"
  ```
4. Run the script: Just fire up the script in your Python environment, and boom! Your files will be neatly organized.

## 🧠 What Does This Script Do?

- Detects photos and videos in a source folder (supports formats like .jpg, .png, .heic, .mp4, etc.).
- Extracts their creation date (using EXIF data when available, or fallback to file metadata).
- Organizes them into folders like 2025-01, 2024-12, etc., in the destination directory.
- Works even for fancy .heic and .heif formats. (Yes, we’re that cool.)

## 🚀 Supported File Formats
- Photos: .jpg, .jpeg, .png, .bmp, .gif, .heic, .heif
- Videos: .mp4, .avi, .mov, .mkv

## ⚠️ Notes
- Make sure the pillow-heif module is installed if you’re dealing with .heic or .heif files.
- Files that don’t have a detectable creation date will be skipped, and you’ll get a friendly error message.

## 💡 Why Use This?
- Because who doesn’t love an organized photo library? Plus, this saves you from the manual pain of sorting everything yourself. 🏖️
