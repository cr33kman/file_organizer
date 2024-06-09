import os
import json

with open("utils/config.json", "r") as f:
    config = json.load(f)


def get_src(sysname) -> str:
    username = os.getlogin()

    src = config["source_paths"].get(sysname, f"/home/{username}/Downloads")
    return src.format(username=username)


def get_dest(file_extension) -> str:
    return config["dest_paths"].get(file_extension, config["default_path"])
