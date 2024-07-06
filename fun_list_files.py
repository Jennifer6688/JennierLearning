# fun_list_files.py
import os

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

directory = "."
print(list_files(directory))
