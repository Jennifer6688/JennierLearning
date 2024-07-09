# fun_remove_vowels.py
def fun_remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

print(fun_remove_vowels('Hello World'))
