# func_py_calculate_bifolium_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_bifolium_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.cos(t) * np.sin(t)
    y = a * np.sin(t)**2
    plt.plot(x, y)
    plt.title("Bifolium Curve")
    plt.show()

func_py_calculate_bifolium_curve(5, 1000)
