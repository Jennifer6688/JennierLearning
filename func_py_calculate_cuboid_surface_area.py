# func_py_calculate_cuboid_surface_area.py
def func_py_calculate_cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

print(func_py_calculate_cuboid_surface_area(3, 4, 5))
