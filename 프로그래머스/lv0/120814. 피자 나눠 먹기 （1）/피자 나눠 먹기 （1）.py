import math
def solution(n):
    return math.ceil(n/7)

# (n - 1) // 7 + 1
# (n//7) + ( 1 if math.ceil(n%7)>0 else 0)