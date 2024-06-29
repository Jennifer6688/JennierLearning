# generate_random_color.py
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    print(f"Random color: {random_color()}")
