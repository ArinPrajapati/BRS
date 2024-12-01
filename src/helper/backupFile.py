from pathlib import Path
import tarfile
from .encryptFile import encrypt_file

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
