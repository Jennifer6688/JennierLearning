# func_py_find_max_string.py
def func_py_find_max_string(lst):
    return max(lst, key=len)

print(func_py_find_max_string(["apple", "banana", "cherry", "date"]))
