import os
import platform
import logging
from utils.path_handler import get_src
from utils.file_operations import move_files

logging.basicConfig(
    level=logging.INFO,
    filename="logs/movelogs.log",
    filemode="a",
    format="[%(asctime)s] - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    sysname = platform.system()
    src_path = input(f"Enter file path ({get_src(sysname)}): ") or get_src(sysname)

    if not os.path.isdir(src_path):
        logger.error(f"Invalid directory: {src_path}")
        return

    move_files(src_path)


if __name__ == "__main__":
    main()
