# func_py_generate_koch_snowflake.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_generate_koch_snowflake(iterations):
    def koch_snowflake(order):
        def divide(p1, p2):
            return (p2 - p1) / 3

        def rotate(v, angle):
            return v * np.exp(1j * angle)

        vertices = np.array([0, 1, np.exp(1j * 2 * np.pi / 3)], dtype=complex)
        snowflake = np.concatenate([vertices, vertices[:1]])

        for _ in range(order):
            new_snowflake = []
            for i in range(len(snowflake) - 1):
                p1, p2 = snowflake[i], snowflake[i + 1]
                v = divide(p1, p2)
                new_snowflake.extend([p1, p1 + v, p1 + v + rotate(v, np.pi / 3), p1 + 2 * v])
            snowflake = np.array(new_snowflake + [snowflake[-1]])
        return snowflake

    plt.plot(np.real(koch_snowflake(iterations)), np.imag(koch_snowflake(iterations)))
    plt.show()

func_py_generate_koch_snowflake(4)
