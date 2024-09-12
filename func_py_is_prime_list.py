# func_py_is_prime_list.py
def func_py_is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def func_py_is_prime_list(lst):
    return [n for n in lst if func_py_is_prime(n)]

print(func_py_is_prime_list([2, 3, 4, 5, 10, 13]))
