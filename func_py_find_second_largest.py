# func_py_find_second_largest.py
def func_py_find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort(reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None

print(func_py_find_second_largest([1, 3, 4, 5, 5, 2, 1]))
