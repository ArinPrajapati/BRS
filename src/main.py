from .helper import logger
import tarfile
import shutil
import os
from pathlib import Path
import subprocess


def encrypt_file(file_path, key):
    try:
        ecnrypted_file = file_path.with_suffix(file_path.suffix + ".enc")

        subprocess.run(
            [
                "openssl",
                "enc",
                "-aes-256-cbc",
                "-salt",
                "-in",
                str(file_path),
                "-out",
                ecnrypted_file,
                "-k",
                key,
            ],
            check=True,
        )

        print(f"File {file_path} has been encrypted to {ecnrypted_file}")
        return ecnrypted_file
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False


def backup_file(file_path, backup_path, key=None):
    try:

        file_path = Path(file_path)
        output_path = Path(backup_path)

        # Check if the file exists before proceeding
        if not file_path.exists():
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        if output_path.is_dir():
            output_path = output_path / f"{file_path.name}.tar.gz"
        # Create the parent directory for the backup if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with tarfile.open(output_path, "w:gz") as tar:
            tar.add(file_path, arcname=file_path.name)

        print(f"File {file_path} has been backed up to {output_path}")

        if key:
            encrypted_file = encrypt_file(output_path, key)
            if encrypted_file:
                output_path.unlink()

            return encrypted_file

        return output_path

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


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
