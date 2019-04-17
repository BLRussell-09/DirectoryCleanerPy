#!/usr/bin/python
import os

dir_path = "/home/tiniwraith/workspace/flaskRest/Cleaner"
exts = [".txt", ".md"]

def clean_files(path_to_directory, extensions):
  if len(os.listdir(path_to_directory)) > 0:
    for ext in extensions:
      for file_name in os.listdir(path_to_directory):
        if file_name.endswith(ext):
          os.remove(f"{dir_path}/{file_name}")
          print("File removed!")
  else:
    print("There's nothing here for me :(")

clean_files(dir_path, exts)
