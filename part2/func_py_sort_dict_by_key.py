# func_py_sort_dict_by_key.py

def func_py_sort_dict_by_key(d):
    return dict(sorted(d.items()))

def test_sort_dict_by_key():
    data = {'c': 3, 'a': 1, 'b': 2}
    print(f"Sorted dictionary by key: {func_py_sort_dict_by_key(data)}")

if __name__ == "__main__":
    test_sort_dict_by_key()
