import os
import glob
import shutil
import operator

def create_dir(src):
    folders = ["csv","log","txt"]
    # Implement the directory cleaning functionality here
    for folder in folders:
        path = os.path.join(src, folder)
        os.mkdir(path)

def move_files(dir):
  for file in os.listdir(dir):
    file_path = os.path.join(dir,file)
    if os.path.isfile(file_path):
      if file[-4:]==".txt":
        source = os.path.join(dir,file)
        path = os.path.join(dir,'txt')
        path = os.path.join(path,file)
        shutil.move(source,path)
    
      elif file[-4:]==".log":
        source = os.path.join(dir,file)
        path = os.path.join(dir,'log')
        path = os.path.join(path,file)
        shutil.move(source,path)
    
      elif file[-4:]==".csv":
        source = os.path.join(dir,file)
        path = os.path.join(dir,'csv')
        path = os.path.join(path,file)
        shutil.move(source,path)
      else:
        print(f'Unknown extension: {file}')


def count_files(src):
  count = 0
# Iterate directory
  dir = os.path.join(src, "log")
  for path in os.listdir(dir):
  # check if current path is a file
    if os.path.isfile(os.path.join(dir, path)):
      count += 1
  return int(count)


def recent_log_files(src,number):
  log_folder_path = os.path.join(src, "log")
  files = os.listdir(log_folder_path)
  sorted_files = sorted(files)
  delete = len(sorted_files) - int(number)
  for x in range(0, delete):
    path = os.path.join(log_folder_path,sorted_files[x])
    os.remove(path)

    
def get_txt_file_size(src,file):
  path = os.path.join(src,"txt")
  file_path = os.path.join(path,file)
  file_stats = os.stat(file_path)
  return (file_stats.st_size)/1000 #converting bytes to kilobytes

def make_large_txt_files_dir(src):
    path = os.path.join(src, "txt")
    path = os.path.join(path, "large_txt_files")
    os.mkdir(path)
    return path


def move_large_files(src,file):
  path = os.path.join(src,file)
  dest = os.path.join(src,"txt")
  destination = os.path.join(dest,"large_txt_files")
  destination_file_path = os.path.join(destination,file)
  shutil.move(path,destination_file_path)
    
