import subprocess


def decrypt_file(file_path, key):
    try:
        decrypted_file = file_path.with_suffix(file_path.suffix.replace(".enc", ""))

        subprocess.run(
            [
                "openssl",
                "enc",
                "-d",
                "-aes-256-cbc",
                "-in",
                str(file_path),
                "-out",
                decrypted_file,
                "-k",
                key,
            ],
            check=True,
        )

        print(f"File {file_path} has been decrypted to {decrypted_file}")
        return decrypted_file
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
