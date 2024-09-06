# func_py_calculate_lcm.py
def func_py_calculate_lcm(a, b):
    gcd = func_py_find_gcd(a, b)
    return abs(a * b) // gcd

print(func_py_calculate_lcm(4, 5))
