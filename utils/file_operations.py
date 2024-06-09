import os
import logging
from utils.path_handler import get_dest

logger = logging.getLogger(__name__)


def move_files(src_path):
    try:
        files = [
            f for f in os.listdir(src_path) if os.path.isfile(os.path.join(src_path, f))
        ]

        for file in files:
            ext = file.split(".")[-1]
            dest_path = os.path.join(src_path, get_dest(ext))

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)
                logger.info(f"{dest_path} was created.")

            src = os.path.join(src_path, file)
            dest = os.path.join(dest_path, file)

            os.rename(src, dest)  # Move the file

            logger.info(f"{file} was moved to {dest}.")

    except FileNotFoundError:
        logger.error(f"File {src_path} not found.")
    except PermissionError:
        logger.error(f"Permission denied for {src_path}.")
    except NotADirectoryError:
        logger.error(f"{src_path} is not a directory.")
    except Exception as e:
        logger.error(f"Error: {e}")
