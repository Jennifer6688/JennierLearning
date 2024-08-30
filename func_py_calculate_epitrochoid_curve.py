# func_py_calculate_epitrochoid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_epitrochoid_curve(R, r, d, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = (R + r) * np.cos(t) - d * np.cos((R + r) * t / r)
    y = (R + r) * np.sin(t) - d * np.sin((R + r) * t / r)
    plt.plot(x, y)
    plt.title("Epitrochoid Curve")
    plt.show()

func_py_calculate_epitrochoid_curve(5, 3, 1, 1000)
