# func_py_calculate_hexagonal_prism_surface_area.py
import math

def func_py_calculate_hexagonal_prism_surface_area(side_length, height):
    base_area = (3 * math.sqrt(3) / 2) * side_length**2
    lateral_area = 6 * side_length * height
    return 2 * base_area + lateral_area

print(func_py_calculate_hexagonal_prism_surface_area(6, 10))
