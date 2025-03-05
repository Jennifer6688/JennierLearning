# func_py_find_longest_substring.py
def func_py_find_longest_substring(s):
    substr = ""
    longest = ""
    for char in s:
        if char not in substr:
            substr += char
        else:
            substr = char
        if len(substr) > len(longest):
            longest = substr
    return longest
