# func_py_calculate_toroid_volume.py
import math

def func_py_calculate_toroid_volume(radius_major, radius_minor):
    return (2 * math.pi * radius_minor**2) * (2 * math.pi * radius_major)

print(func_py_calculate_toroid_volume(6, 2))
