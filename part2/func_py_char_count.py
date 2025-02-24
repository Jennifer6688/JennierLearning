# 3. 统计字符串中每个字符的出现次数
from collections import Counter

def char_count(s):
    return dict(Counter(s))

print(char_count("hello world"))  
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
