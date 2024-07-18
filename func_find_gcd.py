# func_find_gcd.py
def func_find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(func_find_gcd(24, 36))
