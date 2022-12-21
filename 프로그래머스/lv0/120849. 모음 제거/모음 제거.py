def solution(my_string):
    return ''.join([ i for i in my_string if not ((i=='a') or (i=='i') or (i=='o') or (i=='e') or (i=='u')) ])

# (i in "aeiou")
