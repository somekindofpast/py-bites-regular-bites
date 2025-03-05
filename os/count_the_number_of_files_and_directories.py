import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dir_num = 0
    file_num = 0
    for root, dirs, files in os.walk(directory):
        dir_num += len(dirs)
        file_num += len(files)
    return dir_num, file_num