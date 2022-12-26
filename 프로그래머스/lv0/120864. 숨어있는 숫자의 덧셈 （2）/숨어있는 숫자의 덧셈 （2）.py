import re

def solution(my_string):
    digits = re.findall(r'\d+', my_string)
    return sum([int(i) for i in digits])