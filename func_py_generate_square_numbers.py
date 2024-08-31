# func_py_generate_square_numbers.py
def func_py_generate_square_numbers(limit):
    square_numbers = [n * n for n in range(1, limit + 1)]
    return square_numbers

print(func_py_generate_square_numbers(10))
