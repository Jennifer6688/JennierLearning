# fun_py_check_vowel.py

def fun_py_check_vowel(ch):
    return ch.lower() in "aeiou"

def test_check_vowel():
    letters = ["a", "b", "e", "z", "o"]
    for letter in letters:
        print(f"'{letter}' is a vowel: {fun_py_check_vowel(letter)}")

if __name__ == "__main__":
    test_check_vowel()
