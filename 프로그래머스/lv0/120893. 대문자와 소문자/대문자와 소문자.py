def solution(my_string):
    return ''.join([ i.lower() if ord(i)<91 else i.upper() for i in my_string ])