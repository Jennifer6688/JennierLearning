# func_is_pangram.py
import string

def func_is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(sentence.lower())

print(func_is_pangram("The quick brown fox jumps over the lazy dog"))
