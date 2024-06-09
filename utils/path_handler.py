import os
import json
import logging

logger = logging.getLogger(__name__)

try:
    with open("utils/config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    logger.error("config.json not found.")
except Exception as e:
    logger.error("Error: {e}.")


def get_src(sysname) -> str:
    if not config:
        return

    try:
        username = os.getlogin()
    except Exception:
        username = os.getenv("USER", "default_user")

    src = config["source_paths"].get(sysname, f"/home/{username}/Downloads")
    return src.format(username=username)


def get_dest(file_extension) -> str:
    if not config:
        return

    return config["dest_paths"].get(file_extension, config["default_path"])
