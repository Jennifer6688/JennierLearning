# func_py_calculate_circular_ring_area.py
import math

def func_py_calculate_circular_ring_area(outer_radius, inner_radius):
    return math.pi * (outer_radius**2 - inner_radius**2)

print(func_py_calculate_circular_ring_area(7, 3))
