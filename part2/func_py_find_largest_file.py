# func_py_find_largest_file.py
import os

def func_py_find_largest_file(directory):
    files = [(f, os.path.getsize(os.path.join(directory, f))) for f in os.listdir(directory)]
    largest = max(files, key=lambda x: x[1], default=None)
    return largest

print(func_py_find_largest_file("."))
