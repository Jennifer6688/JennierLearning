# func_py_reverse_words.py
def func_py_reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(func_py_reverse_words("Hello World from Python"))
