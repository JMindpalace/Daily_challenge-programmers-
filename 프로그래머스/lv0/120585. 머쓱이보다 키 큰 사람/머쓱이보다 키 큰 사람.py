def solution(array, height):
    answer = sum([ 1 if i>height else 0 for i in sorted(array)  ])
    return answer