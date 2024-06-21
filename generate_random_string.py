# generate_random_string.py
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

length = 12
random_string = generate_random_string(length)
print(f"Random String: {random_string}")
