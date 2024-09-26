# func_py_sum_of_digits.py
def func_py_sum_of_digits(n):
    return sum(map(int, str(n)))

print(func_py_sum_of_digits(12345))
