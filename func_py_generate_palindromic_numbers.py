# func_py_generate_palindromic_numbers.py
def func_py_generate_palindromic_numbers(limit):
    return [i for i in range(limit) if str(i) == str(i)[::-1]]

print(func_py_generate_palindromic_numbers(200))
