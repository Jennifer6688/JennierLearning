# func_calculate_distance_3d.py
def func_calculate_distance_3d(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5

print(func_calculate_distance_3d(0, 0, 0, 3, 4, 5))
