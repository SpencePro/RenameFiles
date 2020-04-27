"""rename multiple images in a folder at once, using a consistent numeric rating scheme (891, 892, 893, etc.)"""

import os
from pathlib import Path
from natsort import natsorted

srcFolder = input(Path(r"Enter the file folder: "))
os.chdir(srcFolder)
files = os.listdir(srcFolder)
number = 1

for filename in natsorted(files):
    name, ext = filename.split(".")
    os.rename(filename, str(number) + "." + ext)
    number += 1

print("Done")
