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
    # Generate a random filename
    random_name = f"{uuid.uuid4()}.jpg"  # You can change the extension based on the uploaded file type

    # Create the path to the temporary directory
    tmp_dir = "tmp/"  # On Linux/Mac
    # tmp_dir = "C:\\Temp"  # On Windows

    # Create the temporary directory if it doesn't exist
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    # Save the file to the temporary directory
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
    # Check if the file exists
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
    else:
        print(f"The file '{file_path}' does not exist.")