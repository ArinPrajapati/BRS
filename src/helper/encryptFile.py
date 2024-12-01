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
