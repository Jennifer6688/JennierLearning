# func_py_find_smooth_numbers.py
def func_py_find_smooth_numbers(limit, factor):
    def is_smooth(num):
        while num > 1:
            if num % factor == 0:
                num //= factor
            else:
                return False
        return True
    
    return [n for n in range(2, limit) if is_smooth(n)]

print(func_py_find_smooth_numbers(100, 2))
