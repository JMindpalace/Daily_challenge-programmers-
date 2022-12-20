def solution(sides):
    answer = max(sides)-(sides.pop(sides.index(min(sides)))+sides.pop(sides.index(min(sides))))
    return 1 if answer<0 else 2  