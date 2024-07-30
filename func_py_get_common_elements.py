# func_py_get_common_elements.py
def func_py_get_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(func_py_get_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
