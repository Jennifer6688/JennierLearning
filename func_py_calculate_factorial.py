def func_py_calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * func_py_calculate_factorial(n - 1)
