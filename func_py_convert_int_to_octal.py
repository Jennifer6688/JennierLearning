# func_py_convert_int_to_octal.py
def func_py_convert_int_to_octal(n):
    try:
        return oct(n)
    except TypeError:
        return None

print(func_py_convert_int_to_octal(10))
print(func_py_convert_int_to_octal(255))
