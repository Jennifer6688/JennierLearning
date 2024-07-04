# generate_random_color.py
import random

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

if __name__ == "__main__":
    color = generate_random_color()
    print(f"Generated random color: {color}")
