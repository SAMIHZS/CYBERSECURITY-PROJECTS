import os
import shutil

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

        # prevent scanning folders we create
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

            # duplicate protection
            if os.path.exists(destination_path):

                name, ext = os.path.splitext(file)
                counter = 1

                while os.path.exists(destination_path):
                    new_name = f"{name}({counter}){ext}"
                    destination_path = os.path.join(destination_folder, new_name)
                    counter += 1

            shutil.move(file_path, destination_path)


def main():

    while True:

        folder = input("Enter folder path to organize: ")

        if os.path.isdir(folder):

            organize_files(folder)
            print("Files organized successfully.")

            opt = input("Do you want to organize another folder? (y/n): ")

            if opt.lower() == "n":
                break

        else:
            print("Invalid folder path.")


if __name__ == "__main__":
    main()