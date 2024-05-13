import os
from pathlib import Path

# Input your personal directory path here
directory_path = 'Enter Your Folder Path Here'

for filename in os.listdir(directory_path):
    old_file = Path(directory_path) / filename
    if old_file.is_file():
        new_file = old_file.with_suffix('.txt')
        old_file.rename(new_file)

print("All files have been renamed to .txt")
