# func_py_palindrome_check.py

def func_py_palindrome_check(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def test_palindrome_check():
    words = ["Madam", "Racecar", "Hello"]
    for w in words:
        print(f"'{w}' is palindrome: {func_py_palindrome_check(w)}")

if __name__ == "__main__":
    test_palindrome_check()
