# fun_py_is_prime.py

def fun_py_is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    number = 29
    print(f"Is {number} prime? {fun_py_is_prime(number)}")

if __name__ == "__main__":
    test_is_prime()
