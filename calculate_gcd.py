# calculate_gcd.py
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 56
num2 = 98
gcd = calculate_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd}")
