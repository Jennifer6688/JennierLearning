# func_py_palindrome.py

def func_py_palindrome(word):
    return word == word[::-1]

def test_palindrome():
    print(f"Is 'racecar' a palindrome? {func_py_palindrome('racecar')}")

if __name__ == "__main__":
    test_palindrome()
