# fun_py_sum_of_digits.py

def fun_py_sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def test_sum_of_digits():
    number = 345
    print(f"Sum of digits: {fun_py_sum_of_digits(number)}")

if __name__ == "__main__":
    test_sum_of_digits()
