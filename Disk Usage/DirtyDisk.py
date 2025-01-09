import os
from collections import defaultdict
import matplotlib.pyplot as plt

# Define file categories
file_categories = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp"},
    "Videos": {".mp4", ".avi", ".mov", ".mkv"},
    "Documents": {".pdf", ".docx", ".xlsx", ".txt"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Others": set()
}

# Function to calculate folder sizes and categorize files
def analyze_disk_usage(directory):
    category_sizes = defaultdict(int)
    folder_sizes = defaultdict(int)

    for root, dirs, files in os.walk(directory):
        folder_total = 0
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                folder_total += size

                # Categorize file
                ext = os.path.splitext(file)[1].lower()
                for category, extensions in file_categories.items():
                    if ext in extensions:
                        category_sizes[category] += size
                        break
                else:
                    category_sizes["Others"] += size
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        folder_sizes[root] = folder_total

    return folder_sizes, category_sizes

# Function to visualize data
def visualize_data(category_sizes, folder_sizes):
    # Pie chart for categories
    plt.figure(figsize=(10, 5))
    plt.pie(
        category_sizes.values(),
        labels=category_sizes.keys(),
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.tab20.colors
    )
    plt.title("Disk Usage by File Type")
    plt.show()

    # Bar chart for folder sizes
    folders = list(folder_sizes.keys())
    sizes = list(folder_sizes.values())
    
    # Limit display to top 10 largest folders for readability
    sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)[:10]
    folders, sizes = zip(*sorted_folders) if sorted_folders else ([], [])

    plt.figure(figsize=(12, 6))
    plt.barh(folders, sizes, color="skyblue")
    plt.title("Disk Usage by Folders (Top 10)")
    plt.xlabel("Size (bytes)")
    plt.ylabel("Folders")
    plt.tight_layout()
    plt.show()

# Main function
if __name__ == "__main__":
    print("Welcome to Disk Usage Analyzer")
    directory = input("Enter the directory to analyze: ").strip()

    if not os.path.exists(directory):
        print("The specified directory does not exist. Please try again.")
    else:
        print("Analyzing... This might take a while for large directories.")
        folder_sizes, category_sizes = analyze_disk_usage(directory)

        print("Analysis Complete. Generating visualizations...")
        visualize_data(category_sizes, folder_sizes)

        print("Visualization Complete. Thank you for using Disk Usage Analyzer!")
