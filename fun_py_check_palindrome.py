# fun_py_check_palindrome.py
def fun_py_check_palindrome(string):
    return string == string[::-1]

print(fun_py_check_palindrome("radar"))
print(fun_py_check_palindrome("hello"))
