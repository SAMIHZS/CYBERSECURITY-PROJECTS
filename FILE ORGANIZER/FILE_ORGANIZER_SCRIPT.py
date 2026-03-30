import os
import shutil
import tkinter as tk

file_types = {
    "images": ["png", "jpg", "jpeg", "gif", "bmp", "webp", "tiff", "svg"],
    "videos": ["mp4", "mkv", "mov", "avi", "wmv", "flv", "webm"],
    "documents": ["doc", "docx", "txt", "pdf", "rtf", "odt"],
    "spreadsheets": ["xls", "xlsx", "csv", "ods"],
    "presentations": ["ppt", "pptx", "odp"],
    "audio": ["mp3", "wav", "aac", "flac", "ogg", "m4a"],
    "archives": ["zip", "rar", "7z", "tar", "gz", "bz2"],
    "code": ["py", "js", "java", "cpp", "c", "cs", "php", "html", "css"],
    "executables": ["exe", "msi", "apk", "bat", "sh"],
    "fonts": ["ttf", "otf", "woff", "woff2"],
    "ebooks": ["epub", "mobi", "azw", "azw3"],
    "disk_images": ["iso", "img", "dmg"],
    "databases": ["db", "sqlite", "sql"],
    "configs": ["ini", "cfg", "conf", "yaml", "yml", "json", "toml"],
    "logs": ["log"]
}

def organize_files(base_folder):
    skip_folders = set(file_types.keys()) | {"others"}
    for root, dirs, files in os.walk(base_folder):
        dirs[:] = [d for d in dirs if d not in skip_folders]
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1].lower().lstrip('.')
            category = "others"
            for key, ext_list in file_types.items():
                if extension in ext_list:
                    category = key
                    break
            destination_folder = os.path.join(base_folder, category)
            os.makedirs(destination_folder, exist_ok=True)
            destination_path = os.path.join(destination_folder, file)
            if os.path.exists(destination_path):
                name, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_path):
                    new_name = f"{name}({counter}){ext}"
                    destination_path = os.path.join(destination_folder, new_name)
                    counter += 1
            shutil.move(file_path, destination_path)

def start_organizing():
    folder = entry.get()  # ✅ Get user input from Entry
    if os.path.isdir(folder):
        organize_files(folder)
        result_label.config(text="Files Organized Successfully")
    else:
        result_label.config(text="Invalid folder path")

def main():
    global entry, result_label
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("600x200")

    tk.Label(root, text="Enter folder path to organize:").grid(row=0, column=0, padx=10, pady=10)
    entry = tk.Entry(root, width=50)
    entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(root, text="Organize", command=start_organizing).grid(row=1, column=1, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=2, column=1)

    root.mainloop()

if __name__ == "__main__":
    main()
