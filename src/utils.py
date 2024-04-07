import os
import uuid

from fastapi import UploadFile


def save_file_to_tmp(file: UploadFile) -> str:
    """
    Save the uploaded file to the temporary directory with a random name.

    Args:
        file (UploadFile): The uploaded file.

    Returns:
        str: The path to the saved file.
    """
    random_name = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"

    tmp_dir = "tmp/"

    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    file_path = os.path.join(tmp_dir, random_name)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path


def delete_file(file_path: str):
    """
    Delete the file specified by the given file path.

    Args:
        file_path (str): The path to the file to be deleted.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f"The file '{file_path}' does not exist.")