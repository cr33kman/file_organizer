import os
import platform
from file_formats import get_file_path

username = os.getlogin()
sysname = platform.system()

if sysname == "Linux":
    src_path = f"/home/{username}/Downloads"
elif sysname == "Windows":
    src_path = f"C:/Users/{username}/Downloads"
elif sysname == "Darwin":
    src_path = f"/Users/{username}/Downloads"

src_path = input(f"Enter file path ({src_path}): ") or src_path

files = [f for f in os.listdir(src_path) if os.path.isfile(os.path.join(src_path, f))]

for file in files:
    extension = file.split(".")[-1]
    dest_path = get_file_path(extension)
    dest = src_path + dest_path

    if not os.path.exists(dest) or not os.path.isdir(dest):
        os.makedirs(dest)

    src = src_path + "/" + file
    dest += file
    os.rename(src, dest)

    print(f"{file} was successfully moved to {dest}.")
