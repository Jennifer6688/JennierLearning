# func_py_zip_directory.py
import shutil

def func_py_zip_directory(source_dir, output_zip):
    shutil.make_archive(output_zip, 'zip', source_dir)

func_py_zip_directory("test_folder", "backup")
