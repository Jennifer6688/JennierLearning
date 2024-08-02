# func_py_check_pangram.py
def func_py_check_pangram(string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(string.lower())

print(func_py_check_pangram("The quick brown fox jumps over the lazy dog"))
print(func_py_check_pangram("Hello, World!"))
