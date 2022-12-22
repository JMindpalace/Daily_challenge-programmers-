def solution(my_string):
    return ''.join([ i.lower() if ord(i)<91 else i.upper() for i in my_string ])

# return my_string.swapcase()
# 대소문자 변경 메소드
