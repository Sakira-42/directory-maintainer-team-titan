# Directory Maintainer
# Organizes the files within a directory
# Usage: python3 main.py [path/to/directory] [--log-window=N] [--size-threshold=M]
import argparse
from dir_manager import *
import os

directory = input("Enter directory of files: ")

def clean_directory(directory, log_window, size_threshold):
  create_dir(directory)
  move_files(directory)

  if count_files(directory) > log_window:
    recent_log_files(directory,log_window)
  path = os.path.join(directory,"txt")
  for file in os.listdir(path):
    if get_txt_file_size(directory,file) > size_threshold:
      make_large_txt_files_dir(directory)
      move_large_files(directory,file)



# This code reads the command line arguments and passes them into the
# clean_directory function.
# It sets the defaults for the log window and the size threshold
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean up a messy data directory')
    parser.add_argument('--log-window',
            dest='log_window',
            default=30, # retain 30 log files by default
            type=int, 
            help='log retention policy: how many most recent log files to keep')
    parser.add_argument('--size-threshold',
            dest='size_threshold',
            default=50, # 50KB default
            type=int, 
            help='file size threshold: how large is a large text file')
    log_window = parser.parse_args().log_window
    size_threshold = parser.parse_args().size_threshold

    clean_directory(directory, log_window, size_threshold)
