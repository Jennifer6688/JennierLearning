# func_py_validate_palindrome.py
import re

def func_py_validate_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return s == s[::-1]

print(func_py_validate_palindrome("A man, a plan, a canal: Panama"))
