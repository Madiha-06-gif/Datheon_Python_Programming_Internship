import os
import shutil
import logging
from pathlib import Path
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"]
}
SOURCE_FOLDER = Path("sample_files")
def get_category(file):
    extension = file.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return None
def create_category_folders():
    SOURCE_FOLDER.mkdir(exist_ok=True)

    for category in FILE_CATEGORIES:
        folder_path = SOURCE_FOLDER / category
        folder_path.mkdir(exist_ok=True)

def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            destination.stem
            + f"_{counter}"
            + destination.suffix
        )

        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1

def organize_files():
    moved_count = 0
    skipped_count = 0

    create_category_folders()

    for entry in os.scandir(SOURCE_FOLDER):
        if entry.is_file():
            file_path = Path(entry.path)
            category = get_category(file_path)

            if category is None:
                print(f"Skipped: {file_path.name} (Unknown file type)")
                logging.warning(f"Skipped {file_path.name}: Unknown file type")
                skipped_count += 1
                continue

            destination_folder = SOURCE_FOLDER / category
            destination = destination_folder / file_path.name

            destination = get_unique_destination(destination)

            try:
                shutil.move(str(file_path), str(destination))

                print(f"Moved: {file_path.name} -> {category}")
                logging.info(f"Moved {file_path.name} to {category}")
                moved_count += 1

            except (PermissionError, OSError) as error:
                print(f"Could not move {file_path.name}: {error}")
                logging.error(f"Could not move {file_path.name}: {error}")
                skipped_count += 1

    print("\n----- ORGANIZATION SUMMARY -----")
    print(f"Files moved: {moved_count}")
    print(f"Files skipped: {skipped_count}")
    logging.info(
        f"Organization completed. Moved: {moved_count}, Skipped: {skipped_count}"
    )


if __name__ == "__main__":
    organize_files()