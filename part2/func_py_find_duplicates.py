# func_py_find_duplicates.py
def func_py_find_duplicates(lst):
    return [x for x in set(lst) if lst.count(x) > 1]
