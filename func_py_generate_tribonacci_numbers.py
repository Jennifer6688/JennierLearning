# func_py_generate_tribonacci_numbers.py
def func_py_generate_tribonacci_numbers(n):
    sequence = [0, 1, 1]
    for i in range(3, n):
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    return sequence

print(func_py_generate_tribonacci_numbers(10))
