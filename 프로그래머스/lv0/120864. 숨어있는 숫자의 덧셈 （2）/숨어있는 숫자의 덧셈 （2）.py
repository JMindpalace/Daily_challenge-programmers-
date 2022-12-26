import re

def solution(my_string):
    digits = re.findall(r'\d+', my_string)
    return sum([int(i) for i in digits])

# return sum([int(i) for i in re.findall(r'[0-9]+', my_string

# 공백으로 구분후 합치기
# s = ''.join(i if i.isdigit() else ' ' for i in my_string)
# return sum(int(i) for i in s.split())
