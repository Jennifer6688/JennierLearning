# func_py_sort_dict_by_values.py
def func_py_sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

print(func_py_sort_dict_by_values({'a': 3, 'b': 1, 'c': 2}))
