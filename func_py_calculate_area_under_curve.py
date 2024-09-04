# func_py_calculate_area_under_curve.py
from scipy.integrate import quad

def func_py_calculate_area_under_curve(func, a, b):
    area, _ = quad(func, a, b)
    return area

print(func_py_calculate_area_under_curve(lambda x: x**2, 0, 1))
