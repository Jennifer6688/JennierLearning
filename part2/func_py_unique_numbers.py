# func_py_unique_numbers.py

def func_py_unique_numbers(lst):
    return list(set(lst))

def test_unique_numbers():
    numbers = [1, 2, 2, 3, 4, 4, 5, 5]
    print(f"Unique numbers: {func_py_unique_numbers(numbers)}")

if __name__ == "__main__":
    test_unique_numbers()
