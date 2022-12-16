def solution(array, height):
    return sum([ 1 if i>height else 0 for i in sorted(array) ])


"""
array.append(height)
array.sort(reverse=True)
return array.index(height)
"""