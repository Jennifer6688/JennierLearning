# func_py_check_substring.py
def func_py_check_substring(main_string, sub_string):
    return sub_string in main_string

print(func_py_check_substring("hello world", "world"))
print(func_py_check_substring("hello world", "python"))
