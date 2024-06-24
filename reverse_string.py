# reverse_string.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    reversed_string = reverse_string(string)
    print(f"The reversed string is: {reversed_string}")
