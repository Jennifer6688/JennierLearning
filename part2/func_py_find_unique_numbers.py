# func_py_find_unique_numbers.py

def func_py_find_unique_numbers(lst):
    return list(set(lst))

def test_find_unique_numbers():
    lists = [
        [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9],
        [10, 20, 20, 30, 40, 40, 50],
        [100, 200, 300, 100, 200, 400]
    ]
    for lst in lists:
        print(f"Unique numbers in {lst}: {func_py_find_unique_numbers(lst)}")

if __name__ == "__main__":
    test_find_unique_numbers()
