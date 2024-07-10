# fun_check_palindrome_number.py
def fun_check_palindrome_number(number):
    return str(number) == str(number)[::-1]

print(fun_check_palindrome_number(121))
print(fun_check_palindrome_number(123))
