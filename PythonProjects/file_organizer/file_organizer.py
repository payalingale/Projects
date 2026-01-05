import os
from pathlib import Path
import shutil

# FILE ORGANIZER

# Configuration
SOURCE_DIR = '/Users/payalingale01/duplicate'
DEST_DIR = '/Users/payalingale01/Projects/fileFormatter'
EXTENSIONS = ['.pdf', '.jpg', '.jpeg', '.png', '.xlsx']

# Step 1: Get list of all files in a folder
files = os.listdir(SOURCE_DIR)

# Step 2: For each file, check its extension
ext_list = []
for file in files:
  file_details = Path(file)
  ext_list.append(file_details.suffix)

ext_set = set(ext_list)

# Step 3: Create folders for each file type
print(ext_set)
for ext in ext_set:
  folder_path = os.path.join(DEST_DIR, ext)
  if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# Step 4: Move files to appropriate folders
for file in files:
  file_path = os.path.join(SOURCE_DIR, file)  
  if os.path.isfile(file_path):
    path_file = Path(file)
    if path_file.suffix in EXTENSIONS:
      print(f"Found: {file}")
      dest_path = os.path.join(DEST_DIR, path_file.suffix)
      shutil.move(file_path, dest_path)

# Step 5: Print summary of what was organized
