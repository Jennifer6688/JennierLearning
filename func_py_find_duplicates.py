# func_py_find_duplicates.py
def func_py_find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

print(func_py_find_duplicates([1, 2, 3, 4, 4, 5, 2]))
