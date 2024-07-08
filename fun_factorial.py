# fun_factorial.py
def fun_factorial(n):
    if n == 0:
        return 1
    else:
        return n * fun_factorial(n-1)

print(fun_factorial(5))
