# func_is_palindrome.py
def func_is_palindrome(string):
    return string == string[::-1]

print(func_is_palindrome("racecar"))
print(func_is_palindrome("hello"))
