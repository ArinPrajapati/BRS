from pathlib import Path
import tarfile
from .decrptyFile import decrypt_file


def recover_file(file_path, recover_path, key=None):
    try:
        file_path = Path(file_path)
        output_path = Path(recover_path)

        if not file_path.exists():
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        if output_path.is_dir():
            output_path = output_path / f"{file_path.name.replace('.enc', '')}"

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(output_path.parent)

        print(f"File {file_path} has been recovered to {output_path}")

        if key:
            decrypted_file = decrypt_file(output_path, key)
            if decrypted_file:
                output_path.unlink()

            return decrypted_file

        return output_path

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
