from .helper import logger
import os
from pathlib import Path
from .helper.backupFile import backup_file


def main():

    # Get path of the file and print it
    filePath = input("Enter the path of the file: ")
    filePath = "/home/arin/Downloads/test/file1"  # remove this line
    log = logger.setup_logger(filePath.split("/")[-1])

    log.info(f"File path: {filePath}")

    if not os.path.isabs(filePath):
        log.error(f"File path {filePath} does not exist.")
        print("File path does not exist.")
        return

    # Check if the file actually exists
    if not Path(filePath).exists():
        log.error(f"File {filePath} does not exist.")
        print("File does not exist.")
        return

    print(f"File path: {filePath}")
    print("Starting the backup process...")
    backupPath = input("Enter the path where you want to backup the file: ")
    backupPath = "/home/arin/Downloads/test"  # remove this line
    log.info(f"Backup path: {backupPath}")

    if not os.path.isabs(backupPath):
        log.error(f"Backup path {backupPath} does not exist.")
        print("Backup path does not exist.")
        return

    log.info(f"Copying {filePath} to {backupPath}")

    success = backup_file(filePath, backupPath, "password")
    if success:
        log.info(f"File {filePath} has been backed up to {backupPath}")
    else:
        log.error(f"Failed to backup {filePath} to {backupPath}")


if __name__ == "__main__":
    main()
