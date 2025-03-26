# fun_py_find_factorial.py

def fun_py_find_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def test_find_factorial():
    num = 5
    print(f"Factorial of {num}: {fun_py_find_factorial(num)}")

if __name__ == "__main__":
    test_find_factorial()
