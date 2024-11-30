import logging
import os


def setup_logger(file_name):
    """
     Sets up a logger for each file, creating a log file in the 'logs' directory.

     Args:
    file_name (str): The name of the file being processed (e.g., 'file1.txt').

     Returns:
    logger: A configured logger for the specific file.
    """
    os.makedirs("logs", exist_ok=True)

    log_file = f"logs/{file_name}_log.log"

    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
