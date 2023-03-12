import os


def delete_text_from_files(directory, text_to_delete):
    """
    Rename files in a selected directory that contain a piece of text.

    Args:
    - directory: str, the path of the directory containing the files to modify.
    - text_to_delete: str, the piece of text to search for in the filenames.

    Returns:
    - None.
    """
    # Confirm the directory with the user.
    print(f"WARNING: This program will rename all files in the directory: {directory}")
    response = input("Are you sure you want to proceed? (y/n) ")
    if response.lower() != 'y':
        print("Exiting program.")
        return

    # Change the working directory to the specified directory.
    os.chdir(directory)

    # Get the current working directory.
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")

    # Iterate over the files in the directory.
    for filename in os.listdir('.'):
        # Check if the file is a text file and contains the specified text.
        if filename.endswith('.mp3') and text_to_delete in filename:
            # Construct the new filename by removing the specified text.
            new_filename = filename.replace(text_to_delete, '')
            # Rename the file.
            os.rename(filename, new_filename)
            print(f"Renamed file {filename} to {new_filename}")


# Example usage:
directory = '/example/directory/test'
text_to_delete = 'example text to delete'
delete_text_from_files(directory, text_to_delete)