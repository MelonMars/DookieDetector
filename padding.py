import os
import shutil

def move_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get all the files in the source directory
    files = os.listdir(source_dir)

    # Move each file to the destination directory
    for file_name in files:
        # Get the full path of the source and destination files
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        # Move the file
        shutil.move(source_file, destination_file)

    print("Files moved successfully!")

# Example usage
source_directory = "/content/drive/MyDrive/Excrement/Annotations"
destination_directory = "/content/jetson-inference/python/training/detection/ssd/data/Excrement/Annotations"

move_files(source_directory, destination_directory)
