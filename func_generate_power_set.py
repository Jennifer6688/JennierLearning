# func_generate_power_set.py
from itertools import chain, combinations

def func_generate_power_set(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

print(func_generate_power_set([1, 2, 3]))
