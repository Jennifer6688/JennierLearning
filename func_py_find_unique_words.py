# func_py_find_unique_words.py
def func_py_find_unique_words(text):
    words = text.split()
    return set(words)

print(func_py_find_unique_words("Python is fun, and learning Python is exciting"))
