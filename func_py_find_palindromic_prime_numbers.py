# func_py_find_palindromic_prime_numbers.py
def func_py_find_palindromic_prime_numbers(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    return [n for n in range(2, limit) if is_prime(n) and str(n) == str(n)[::-1]]

print(func_py_find_palindromic_prime_numbers(1000))
